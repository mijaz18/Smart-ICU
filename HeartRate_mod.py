##!/usr/bin/env python3
## -*- coding: utf-8 -*-
#"""
#Created on Tue May 29 15:03:34 2018
#
#@author: muhammadusamaijaz
#"""
#
#import numpy as np
#import pandas as pd
#from sqlalchemy import create_engine
#mimic_db = create_engine("mysql+mysqldb://osama:"+'osama'+"@10.103.76.84/mimic_th")
#sub=99781
#item_id=211
#de=pd.read_sql("SELECT ADMITTIME FROM ADMISSIONS WHERE SUBJECT_ID=%(sub_id)s",con=mimic_db,params={'sub_id': sub})
#pd.data
## -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:34:41 2018
 
@author: zulqarnain
"""
 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector
import datetime as dt
from sqlalchemy import create_engine
mimic_db_demo = create_engine("mysql+mysqldb://osama:"+'osama'+"@10.103.76.53/mimic_worst_values_a")
mimic_db_demp = create_engine("mysql+mysqldb://osama:"+'osama'+"@10.103.76.53/mimic_th")
 
 
#chart_values = pd.read_sql("SELECT ROW_ID, CHARTTIME, VALUE FROM CHARTEVENTS WHERE SUBJECT_ID=%(id)s AND ITEMID=%(itemID)s", params={'id':patient_id,'itemID':item_id}, con=mimic_db_demo)
#df = chart_values
#import datetime as dt
#x = df[df['CHARTTIME']<=(df.CHARTTIME[0]+dt.timedelta(days=1))]['VALUE']
#x = pd.to_numeric(x)
#print ('Patient Id is ', patient_id, ' and Item ID is: ',item_id)
#print ('Min value is: ',min(x))
#print ('Max value is: ',max(x))
ids=pd.read_sql("SELECT SUBJECT_ID FROM PATIENTS",con=mimic_db_demp)

ids['MAX_VALUE']=0
ids['MIN_VALUE']=0
#ids.dr
item_id = 220045
for i in range(887, 1000):
     print('Current Loop no is: ',i)
     if (i == 239):
         i=i+1;
     patient_id= ids.iloc[i]['SUBJECT_ID']
     df = pd.read_sql("SELECT ROW_ID, CHARTTIME, VALUE FROM CHARTEVENTS WHERE SUBJECT_ID=%(id)s AND ITEMID=%(itemID)s", params={'id':patient_id,'itemID':item_id}, con=mimic_db_demp)
     x = df[df['CHARTTIME']<=(df.CHARTTIME[0]+dt.timedelta(days=1))]['VALUE']
     x = pd.to_numeric(x)
     max_val= max(x)
     min_val= min(x)
     ids['MAX_VALUE'].iloc[i]=max_val
     ids['MIN_VALUE'].iloc[i]=min_val
     #ids.to_sql('HEARTRATE',con=mimic_db_demo)
#ids.drop_duplicates(subset=['SUBJECT_ID'],keep='first')
#de=de.drop_duplicates(subset=['SUBJECT_ID'], keep='first')