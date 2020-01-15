#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 15:31:01 2018

@author: muhammadusamaijaz
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
mimic_db = create_engine("mysql+mysqldb://mimic:"+'mimic'+"@adcom.mmzzhh.com/mimic_full")
df=pd.read_sql("SELECT * FROM ADMISSIONS WHERE DEATHTIME IS NOT NULL AND HOSPITAL_EXPIRE_FLAG=0 ",con=mimic_db)
dE=pd.read_sql("SELECT * FROM ADMISSIONS WHERE DEATHTIME IS NULL AND HOSPITAL_EXPIRE_FLAG=1 ",con=mimic_db)