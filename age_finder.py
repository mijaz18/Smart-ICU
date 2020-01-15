#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 12:00:53 2018

@author: zulqarnain
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
#mimic_db = create_engine("mysql+mysqldb://mimic:"+'mimic'+"@www.mmzzhh.com/mimic")

#mimic_db_demo = create_engine("mysql+mysqldb://mimic_demo:"+'mimic_demo@12345'+"@10.103.76.154/mimic_demo")


mimic_db = create_engine("mysql+mysqldb://mimic_demo:"+'mimic_demo@12345'+"@adcom.mmzzhh.com/mimic_demo")
age_dataset = pd.read_sql("SELECT p.subject_id, p.dob, a.hadm_id, a.admittime, p.expire_flag FROM ADMISSIONS a INNER JOIN PATIENTS p ON p.subject_id = a.subject_id", con=mimic_db)
#gender = pd.read_sql("SELECT COUNT(*) FROM PATIENTS WHERE gender = 'M'", con=mimic_db) 

DOB = pd.read_sql("SELECT SUBJECT_ID, DOB FROM PATIENTS", con=mimic_db)
admit_time = pd.read_sql("SELECT SUBJECT_ID, ADMITTIME FROM ADMISSIONS", con=mimic_db)
admit_time = admit_time.drop_duplicates(['SUBJECT_ID'])

merge_data = pd.merge(admit_time, DOB, on='SUBJECT_ID')

dob_array = pd.to_datetime(merge_data['DOB'])
admit_array = pd.to_datetime(merge_data['ADMITTIME'])

age = (abs(dob_array - admit_array) / np.timedelta64(1, 'D')/365)

patients = pd.read_sql("SELECT * FROM PATIENTS", con=mimic_db)
patients['Age'] = age

#patients.to_sql(con=mimic_db, name='PATIENTS', if_exists='replace', index=False)

#chart_info = pd.read_sql("SELECT * FROM CHARTEVENTS WHERE SUBJECT_ID=10006", con = mimic_db)
#bpm_info = pd.read_sql("SELECT * FROM CHARTEVENTS WHERE SUBJECT_ID=10013 AND ITEMID=618", con = mimic_db)
