#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 15:59:01 2018

@author: muhammadusamaijaz
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector
import datetime as dt
from sqlalchemy import create_engine
#mimic_db_demo = create_engine("mysql+mysqldb://osama:"+'osama'+"@10.103.76.53/mimic_worst_values_a")
#mimic_db_demp = create_engine("mysql+mysqldb://osama:"+'osama'+"@10.103.76.53/mimic_th")
#ids=pd.read_sql("SELECT SUBJECT_ID FROM PATIENTS",con=mimic_db_demp)
score=-1

def Temperature(x):
  if x < 33:
      score = 20
  elif x < 33.5:
      score = 16
  elif x < 34:
      score = 13
  elif x < 35:
      score = 8
  elif x < 36:
      score = 2
  elif x < 40:
      score = 0
  else:
      score = 4
    return score
def MAP(x):
  if x <= 39:
        score = 23
  elif x < 60:
      score = 15
  elif x < 70:
      score = 7
  elif x < 80:
      score = 6
  elif x < 100:
      score = 0
  elif x < 120:
      score = 4
  elif x < 130:
      score = 7
  elif x < 140:
      score = 9
  else:
      score = 10
    return score
def HeartRate(hr):
  if hr < 40:
       score = 8
  elif hr < 50:
      score= 5
  elif hr < 100:
      score = 0
  elif hr < 110:
      score = 1
  elif hr < 120:
      score = 5
  elif hr < 140:
      score = 7
  elif hr < 155:
      score = 13
  else:
      score= 17
    return score
def RespiratoryRate(rr):
    if rr <= 5:
      score = 17
  elif rr < 12:
      score = 8
  elif rr < 14:
      score = 7
  elif rr < 25:
      score = 0
  elif rr < 35:
      score = 6
  elif rr < 40:
      score = 9
  elif rr < 50:
      score = 11
  else:
      sco += 18
    return score
def ArterialpH(pha,pco):
  if pha < 7.2:
     if pco < 50:
        score = 12
	else:
        score= 4
  elif pha < 7.3:
	if pco < 30:
        score = 9
	elif pco < 40:
        score = 6
	elif pco < 50:
        score = 3
	else:
        score = 2
  elif pha < 7.35:
	if pco < 30:
        score = 9
	elif pco < 45:
        score = 0
	else: 
        score = 1
  elif pha < 7.45:
	if pco < 30:
        score = 5
	elif pco < 45:
        score = 0
	else:
        score = 1
  elif pha < 7.5:
	if pco < 30:
        score = 5
	elif pco < 35:
        score = 0
	elif pco < 45:
        score = 2
	else:
        score = 12
  elif pha < 7.6:
	if pco < 40:
        score = 3
	else:
        score = 12
  else: 
	if pco < 25:
        score = 0
	if pco < 40:
        score = 3	
	else:
        score = 12
    return score
def SerumSodium(nas):
  if nas < 120:
      score = 3
  elif nas < 135:
      score = 2
  elif nas < 155:
      score = 0
  else: 
      score = 4
    return score
#def SerumPotassium(x):
#    if x>= 130 and x<=149:
#        score=0;
#    elif x>=150 and x<=154:
#        score=1;
#    elif x>=155 and x<=159:
#        score=2;
#    elif x>=160 and x<=179:
#        score=3;
#    elif x>=180:
#        score=4;
#    elif x>=120 and x<=129:
#        score=2;
#    elif x>=111 and x<=119:
#        score=3;
#    elif x<=110:
#        score=4;
#    print("SerumPotassium SCORE: ",score)
#    return score
def SerumCreatinine(hem,uri,cre):
    if hem == 1:
        if uri < 410 and cre >= 1.5:
            score = 10
	else:
	  if cre < 0.5:
          score = 3
      elif cre < 1.5:
          score = 0
      elif cre < 1.95:
          score = 4
      else:
          score = 7
	  
   if hem == 2:
       if cre < 0.5:
           score = 3
    elif cre < 1.5:
        score = 0
    elif cre < 1.95:
        score = 4
    else:
        score = 7
    return score
def  Hematocrit(hto):
    if hto < 41:
        score = 3
  elif hto < 50:
      score = 0
  else:
      score = 3
  return score
def WBC(wbc):
    if wbc < 1:
        score = 19
  elif wbc < 3:
      score = 5
  elif wbc < 20:
      score = 0
  elif wbc < 25:
      score = 1
  else:
      score = 5
  return score
def GCS(x,y,z):
    gcs=x+y+z;
    score=15-gcs;
    print("GCS SCORE: ",score)
    return score
#def SerumHCO3(x):
#    if x>= 22 and x<=31.9:
#        score=0;
#    elif x>=32 and x<=40.9:
#        score=1;
#    elif x>=41 and x<=51.9:
#        score=3;
#    elif x>=160 and x<=179:
#        score=3;
#    elif x>=52:
#        score=4;
#    elif x>=18 and x<=21.9:
#        score=2;
#    elif x>=15 and x<=17.9:
#        score=3;
#    elif x<=15:
#        score=4;
#    print("SerumHCO3 SCORE: ",score)
#    return score
def Age(age):
    if age < 45:
        score = 0
    elif age < 60:
        score = 5
    elif age < 65:
        score = 11
    elif age < 70:
        score = 13
    elif age < 75:
        score = 16
    elif age < 85:
        score = 17
    else:
        score = 24
    return score
def uri(x):
  if x < 400  :
      score = 15
  elif x < 600 :
      score =8
  elif x < 900 :
      score = 7
  elif x < 1500:
      score = 5
  elif x < 2000:
      score = 4
  elif x < 4000:
      score = 0
  else:
      score = 1
  return score
def ure(x):
  if x < 17:
        score = 0
  elif x < 20:
      score = 2
  elif x < 40:
      score = 7
  elif x < 80:
      score = 11
  else:
      score = 12
  return score
def bsl(x):
  if x < 40:
       score = 8
  elif x < 60:
      score = 9
  elif x < 200:
      score = 0
  elif x < 350:
      score = 3
  else :
      score = 5
  return score
def alb(x):
  if x < 20:
        score = 11
  elif x < 25:
      score = 6
  elif x < 45:
      score = 0
  else: 
      score = 4
  return score
def bil(x):
  if x < 2:
        score = 0
  elif x < 3:
      score = 5
  elif x < 5:
      score += 6
  elif x < 8:
      score = 8
  else:
      score = 16
  return score

#def APS(temp,MAP,HeartRate,RespiratoryRate,ArterialpH,Sodium,Potassium,Creatinine,Hematocrit,WBC,GCS,HCO3):
#    score= Temperature(temp)+MAP(MAP)+RespiratoryRate(RespiratoryRate)+ArterialpH(ArterialpH)+SerumSodium(Sodium)+SerumPotassium(Potassium)+
#z=Temperature(31.5)
#MAP(108)
#HeartRate(111)
#RespiratoryRate(10)
#ArterialpH(7.3)
#SerumSodium(125)
#print(bil(9))
