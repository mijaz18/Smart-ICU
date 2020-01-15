#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 15:41:20 2018

@author: muhammadusamaijaz
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
mimic_db = create_engine("mysql+mysqldb://osama:"+'osama'+"@adcom.mmzzhh.com/mimic_th")
df=pd.read_sql("SELECT SUBJECT_ID, ADMISSION_TYPE FROM ADMISSIONS WHERE ADMISSION_TYPE='EMERGENCY'",con=mimic_db)
de=pd.read_sql("SELECT SUBJECT_ID FROM SERVICES WHERE CURR_SERVICE='SURG'",con=mimic_db)
ds=pd.merge(df,de,on='SUBJECT_ID')
ds=ds.drop_duplicates(subset='SUBJECT_ID',keep='first')
