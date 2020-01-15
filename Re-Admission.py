#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 15:01:20 2018

@author: muhammadusamaijaz
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
mimic_db = create_engine("mysql+mysqldb://mimic:"+'mimic'+"@adcom.mmzzhh.com/mimic_5_b")
mimic_filtered = create_engine("mysql+mysqldb://mimic:"+'mimic'+"@203.135.63.87/mimic_filtered_b")
mimic_ds=create_engine("mysql+mysqldb://mimic:"+'mimic'+"@adcom.mmzzhh.com/mimic_5_a")
mimic_filtered_ds = create_engine("mysql+mysqldb://mimic:"+'mimic'+"@203.135.63.87/mimic_filtered_a")
ds=pd.read_sql("SELECT SUBJECT_ID,ADMITTIME FROM ADMISSIONS",con=mimic_ds)
dt=ds[ds.duplicated(subset="SUBJECT_ID",keep=False)]
dt=dt.drop_duplicates(subset="SUBJECT_ID",keep='first')
dt=dt.rename(columns={'SUBJECT_ID': 'subject_ids'})
merge_a=pd.read_sql("SELECT subject_ids FROM filtered_subjects",con=mimic_filtered_ds)
merge_a=pd.merge(dt,merge_a,on='subject_ids')
df=pd.read_sql("SELECT SUBJECT_ID,ADMITTIME FROM ADMISSIONS",con=mimic_db)
de=df[df.duplicated(subset="SUBJECT_ID",keep=False)]
de=de.drop_duplicates(subset="SUBJECT_ID",keep='first')
de=de.rename(columns={'SUBJECT_ID': 'subject_ids'})
merge_b=pd.read_sql("SELECT subject_ids FROM filtered_subjects",con=mimic_filtered)
merge_b=pd.merge(de,merge_b,on='subject_ids')
bigdata = pd.concat([merge_a, merge_b], ignore_index=True)
bigdata= bigdata.drop('ADMITTIME',1)
bigdata.to_csv('Re-Admissions_a_b.csv',sep='\t', encoding='utf-8')