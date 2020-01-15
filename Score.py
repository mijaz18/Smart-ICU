#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 15:59:01 2018

@author: muhammadusamaijaz
"""

def Temperature(x):
    if x>= 36 and x<=38.4:
        score=0;
    elif x>=34 and x<=35.9:
        score=1;
    elif x>=32 and x<=33.9:
        score=2;
    elif x>=30 and x<=31.9:
        score=3;
    elif x<=29.9:
        score=4;
    elif x>=38.5 and x<=38.9:
        score=1;
    elif x>=39 and x<=40.9:
        score=3;
    elif x>=41:
        score=4;
#    print("Temperature SCORE: ",score)
    return score
def MAP(x):
    if x>= 70 and x<=109:
        score=0;
    elif x>=50 and x<=69:
        score=2;
    elif x<=49:
        score=4;
    elif x>=110 and x<=129:
        score=2;
    elif x>=130 and x<=159:
        score=3;
    elif x>=160:
        score=4;
#    print("MAP SCORE: ",score)
    return score
def HeartRate(x):
    if x>= 70 and x<=109:
        score=0;
    elif x>=55 and x<=69:
        score=2;
    elif x>=40 and x<=54:
        score=3;
    elif x<=39:
        score=4;
    elif x>=110 and x<=139:
        score=2;
    elif x>=140 and x<=179:
        score=3;
    elif x>=180:
        score=4;
#    print("HeartRate SCORE: ",score)
    return score
def RespiratoryRate(x):
    if x>= 12 and x<=24:
        score=0;
    elif x>=10 and x<=11:
        score=1;
    elif x>=6 and x<=9:
        score=2;
    elif x<=5:
        score=4;
    elif x>=25 and x<=34:
        score=1;
    elif x>=35 and x<=49:
        score=3;
    elif x>=50:
        score=4;
#    print("RespiratoryRate SCORE: ",score)
    return score
def ArterialpH(x):
    if x>= 7.33 and x<=7.49:
        score=0;
    elif x>=7.25 and x<=7.32:
        score=2;
    elif x>=7.15 and x<=7.24:
        score=3;
    elif x<7.15:
        score=4;
    elif x>=7.5 and x<=7.59:
        score=1;
    elif x>=7.6 and x<=7.69:
        score=3;
    elif x>=7.7:
        score=4;
#    print("ArterialpH SCORE: ",score)
    return score
def SerumSodium(x):
    if x>= 130 and x<=149:
        score=0;
    elif x>=150 and x<=154:
        score=1;
    elif x>=155 and x<=159:
        score=2;
    elif x>=160 and x<=179:
        score=3;
    elif x>=180:
        score=4;
    elif x>=120 and x<=129:
        score=2;
    elif x>=111 and x<=119:
        score=3;
    elif x<=110:
        score=4;
#    print("SerumSodium SCORE: ",score)
    return score
def SerumPotassium(x):
    if x>= 3.5 and x<=5.4:
        score=0;
    elif x>=3 and x<=3.4:
        score=1;
    elif x>=2.5 and x<=2.9:
        score=2;
    elif x>=5.5 and x<=5.9:
        score=1;
    elif x>=7:
        score=4;
    elif x>=6 and x<=6.9:
        score=3;
    elif x<2.5:
        score=4;
#    print("SerumPotassium SCORE: ",score)
    return score
def SerumCreatinine(x):
    if x>=0.6 and x<=1.4:
        score=0;
    elif x>=1.5 and x<=1.9:
        score=2;
    elif x>=2 and x<=3.4:
        score=3;
    elif x>=3.5:
        score=4;
    elif x<0.6:
        score=2;
#    print("SerumCreatininine SCORE: ",score)
    return score
def  Hematocrit(x):
    if x>= 30 and x<=45.9:
        score=0;
    elif x>=20 and x<=29.9:
        score=2;
    elif x>=46 and x<=49.9:
        score=1;
    elif x>=50 and x<=59.9:
        score=2;
    elif x>=60:
        score=4;
    elif x<20:
        score=4;
#    print("Hematocrit SCORE: ",score)
    return score
def WBC(x):
    if x>= 3 and x<=14.9:
        score=0;
    elif x>=1 and x<=2.9:
        score=2;
    elif x>=15 and x<=19.9:
        score=1;
    elif x>=20 and x<=39.9:
        score=2;
    elif x>=40:
        score=4;
    elif x<1:
        score=4;
#    print("WBC SCORE: ",score)
    return score
def GCS(x,y,z):
    gcs=x+y+z;
    score=15-gcs;
#    print("GCS SCORE: ",score)
    return score
def SerumHCO3(x):
    if x>= 22 and x<=31.9:
        score=0;
    elif x>=32 and x<=40.9:
        score=1;
    elif x>=41 and x<=51.9:
        score=3;
    elif x>=160 and x<=179:
        score=3;
    elif x>=52:
        score=4;
    elif x>=18 and x<=21.9:
        score=2;
    elif x>=15 and x<=17.9:
        score=3;
    elif x<=15:
        score=4;
#    print("SerumHCO3 SCORE: ",score)
    return score
def Age(x):
    if x<=44:
        score=0;
    elif x>=45 and x<=54:
        score=2
    elif x>=55 and x<=64:
        score=3
    elif x>=65 and x<=74:
        score=5
    elif x>=75:
        score=6
    return score
def APS(temp,MAP,HeartRate,RespiratoryRate,ArterialpH,Sodium,Potassium,Creatinine,Hematocrit,WBC,GCS,HCO3):
    score= Temperature(temp)+MAP(MAP)+RespiratoryRate(RespiratoryRate)+ArterialpH(ArterialpH)+SerumSodium(Sodium)+SerumPotassium(Potassium)+SerumCreatinine(Creatinine)+Hematocrit(Hematocrit)+WBC(WBC)+GCS(GCS)+SerumHCO3(HCO3)
    return score
