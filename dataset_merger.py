# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 16:02:10 2018

@author: zulqarnain
"""

import pandas as pd


data_a = pd.read_csv('dataset_mimic_a_NV_po2.csv')
data_b = pd.read_csv('dataset_mimic_b_NV_po2.csv')
data_c = pd.read_csv('dataset_mimic_c_NV_po2.csv')



#data_readmissions_index = pd.read_csv('Re-Admissions_a_b.csv')

merge = pd.concat([data_b,data_a],axis=0)
merge = pd.concat([data_c,merge],axis=0)
merge.set_index("subject_ids", inplace=True)

#ids = data_readmissions_index.iloc[:,-1].values;
#merge.drop(ids,inplace=True)


merge.to_csv('dataset_without_score_with_map_maph_merged.csv')




