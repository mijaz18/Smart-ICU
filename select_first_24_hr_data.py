# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:34:41 2018

@author: zulqarnain
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
mimic_db_demo = create_engine("mysql+mysqldb://mimic:"+'mimic'+"@10.103.76.84/mimic_th")

patient_id = 99939
item_id = 220045


chart_values = pd.read_sql("SELECT ROW_ID, CHARTTIME, VALUE FROM CHARTEVENTS WHERE SUBJECT_ID=%(id)s AND ITEMID=%(itemID)s", params={'id':patient_id,'itemID':item_id}, con=mimic_db_demo)
df = chart_values
import datetime as dt
x = df[df['CHARTTIME']<=(df.CHARTTIME[0]+dt.timedelta(days=1))]['VALUE']
x = pd.to_numeric(x)
print ('Patient Id is ', patient_id, ' and Item ID is: ',item_id)
print ('Min value is: ',min(x))
print ('Max value is: ',max(x))
