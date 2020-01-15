#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 15:00:38 2018

@author: muhammadusamaijaz
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
#mimic_db = create_engine("mysql+mysqldb://mimic:"+'mimic'+"@www.mmzzhh.com/mimic")

#mimic_db_demo = create_engine("mysql+mysqldb://mimic_demo:"+'mimic_demo@12345'+"@10.103.76.154/mimic_demo")


mimic_db = create_engine("mysql+mysqldb://mimic:"+'mimic'+"@adcom.mmzzhh.com/mimic_5_a")
#age_dataset = pd.read_sql("SELECT p.subject_id, p.dob, a.hadm_id, a.admittime, p.expire_flag, a.ADMISSION_TYPE FROM ADMISSIONS a INNER JOIN PATIENTS p ON p.subject_id = a.subject_id", con=mimic_db)


DOB = pd.read_sql("SELECT SUBJECT_ID, DOB FROM PATIENTS", con=mimic_db)
admit_time = pd.read_sql("SELECT SUBJECT_ID, ADMITTIME FROM ADMISSIONS", con=mimic_db)
admission_type = pd.read_sql("SELECT SUBJECT_ID, ADMISSION_TYPE FROM ADMISSIONS", con=mimic_db)
expire_flag = pd.read_sql("SELECT SUBJECT_ID, HOSPITAL_EXPIRE_FLAG FROM ADMISSIONS", con=mimic_db)
admit_time = admit_time.drop_duplicates(['SUBJECT_ID'])
admission_type = admission_type.drop_duplicates(['SUBJECT_ID'])
expire_flag = expire_flag.drop_duplicates(['SUBJECT_ID'])

merge_data = pd.merge(admit_time, DOB, on='SUBJECT_ID')

dob_array = pd.to_datetime(merge_data['DOB'])
admit_array = pd.to_datetime(merge_data['ADMITTIME'])

age = round((abs(dob_array - admit_array) / np.timedelta64(1, 'D')/365))

patients = pd.read_sql("SELECT * FROM PATIENTS", con=mimic_db)
columns_to_drop = ['DOD','ROW_ID','DOB','GENDER','DOD_HOSP','DOD_SSN','EXPIRE_FLAG']
patients = patients.drop(columns_to_drop,axis=1)
patients['Age'] = age
patients = pd.merge(admission_type, patients, on='SUBJECT_ID')
patients = pd.merge(expire_flag, patients, on='SUBJECT_ID')
#patients=patients.drop(patients[patients.Age >89].index)
#patients.reset_index(inplace=True)
patients.to_sql(con=mimic_db, name='PATIENTS_AGE', if_exists='replace', index=False)

#chart_info = pd.read_sql("SELECT * FROM CHARTEVENTS WHERE SUBJECT_ID=10006", con = mimic_db)
#bpm_info = pd.read_sql("SELECT * FROM CHARTEVENTS WHERE SUBJECT_ID=10013 AND ITEMID=618", con = mimic_db)

