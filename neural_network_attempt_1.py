# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 14:37:54 2018

@author: zulqarnain
"""


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

## Force Keras to use CPU only
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

# Importing the dataset
dataset = pd.read_csv('df_patients_expiry_fix_without_timestamp_fix.csv')
col_list= list(dataset)
col_list.remove('subject_ids')
#col_list.remove('Expiry_Status')
#col_list.remove('AGE')
#col_list.remove('Admission_Type')
#col_list.remove('GCS')
#col_list.remove('Serum_HCO3')
#col_list.remove('Hematocrit')
#col_list.remove('Serum_Sodium')
#col_list.remove('Serum_Potassium')
#col_list.remove('Serum_Creatinine')
#col_list.remove('White_Blood_Cells')
#col_list.remove('Heart_Rate_Score')
#col_list.remove('Temperature')
#col_list.remove('Repsiratory_Rate')
#col_list.remove('Platelet_Count')
#col_list.remove('BUN')
col_list.remove('Expiry_Status')

X = dataset[col_list].values;

F_size = X.shape[1];

y = dataset.iloc[:, -1].values

# Taking care of missing data
#from sklearn.preprocessing import Imputer
#imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
#imputer = imputer.fit(X[:, 0:F_size+1])
#X[:, 0:F_size+1] = imputer.transform(X[:, 0:F_size+1])

## Encoding categorical data
#from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#labelencoder_X_1 = LabelEncoder()
#X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
#labelencoder_X_2 = LabelEncoder()
#X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
#onehotencoder = OneHotEncoder(categorical_features = [1])
#X = onehotencoder.fit_transform(X).toarray()
#X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

## Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


import keras
from keras.models import Sequential
from keras.layers import Dense
import time
start_time = time.time()

# Initialising the ANN
classifier = Sequential()


classifier.add(Dense(output_dim = round((F_size+1)/2), init = 'uniform', activation = 'relu', input_dim = F_size))

classifier.add(Dense(output_dim = round((F_size+1)/2), init = 'uniform', activation = 'relu'))
classifier.add(Dense(output_dim = round((F_size+1)/2), init = 'uniform', activation = 'relu'))
classifier.add(Dense(output_dim = round((F_size+1)/2), init = 'uniform', activation = 'relu'))

classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))

classifier.compile(optimizer = 'nadam', loss = 'binary_crossentropy', metrics = ['accuracy'])

classifier.fit(X_train, y_train, batch_size = 10, nb_epoch = 100)

y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

print("--- %s seconds ---" % (time.time() - start_time))
# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
accuracy = ((cm[0,0]+cm[1,1])/np.sum(cm))*100;
print("The accuracy is: ",accuracy)
