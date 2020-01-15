#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 17:32:52 2018

@author: muhammadusamaijaz
"""

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
	
def GCS(x,y,z):
    gcs=x+y+z;
    score=15-gcs;
#    print("GCS SCORE: ",score)
    return score

def PO2(minn,maxx):
    x=minn
    y=maxx
    diff_min=abs(x-80)
    diff_max=abs(y-100)
    if diff_min>=diff_max :
        return minn
    elif diff_min<diff_max :
        return maxx
    
def Temperature(minn,maxx):
    x=minn
    y=maxx
    diff_min=abs(x-36)
    diff_max=abs(y-38.4)
    if diff_min>=diff_max :
        return minn
    elif diff_min<diff_max :
        return maxx
def HeartRate(minn,maxx):
    x=minn
    y=maxx
    diff_min=abs(x-70)
    diff_max=abs(y-100)
    if diff_min>=diff_max :
        return minn
    elif diff_min<diff_max :
        return maxx
def MAP(minn,maxx):
    x=minn
    y=maxx
    diff_min=abs(x-70)
    diff_max=abs(y-109)
    if diff_min>=diff_max :
        return minn
    elif diff_min<diff_max :
        return maxx
def RR(minn,maxx):
    x=minn
    y=maxx
    diff_min=abs(x-12)
    diff_max=abs(y-24)
    if diff_min>=diff_max :
        return minn
    elif diff_min<diff_max :
        return maxx
def ArterialpH(minn,maxx):
    x=minn
    y=maxx
    diff_min=abs(x-7.33)
    diff_max=abs(y-7.49)
    if diff_min>=diff_max :
        return minn
    elif diff_min<diff_max :
        return maxx
def Sodium(minn,maxx):
    x=minn
    y=maxx
    diff_min=abs(x-130)
    diff_max=abs(y-149)
    if diff_min>=diff_max :
        return minn
    elif diff_min<diff_max :
        return maxx
def Potassium(minn,maxx):
    x=minn
    y=maxx
    diff_min=abs(x-3.5)
    diff_max=abs(y-5.4)
    if diff_min>=diff_max :
        return minn
    elif diff_min<diff_max :
        return maxx
def Creatinine(minn,maxx):
    x=minn
    y=maxx
    diff_min=abs(x-0.6)
    diff_max=abs(y-1.4)
    if diff_min>=diff_max :
        return minn
    elif diff_min<diff_max :
        return maxx
def Hematocrit(minn,maxx):
    x=minn
    y=maxx
    diff_min=abs(x-30)
    diff_max=abs(y-45.9)
    if diff_min>=diff_max :
        return minn
    elif diff_min<diff_max :
        return maxx
def WBC(minn,maxx):
    x=minn
    y=maxx
    diff_min=abs(x-3)
    diff_max=abs(y-14.9)
    if diff_min>=diff_max :
        return minn
    elif diff_min<diff_max :
        return maxx
def HCO3(minn,maxx):
    x=minn
    y=maxx
    diff_min=abs(x-22)
    diff_max=abs(y-31.9)
    if diff_min>=diff_max :
        return minn
    elif diff_min<diff_max :
        return maxx
def AGE(minn,maxx):
    x=minn
    y=maxx
    diff_min=abs(x-0)
    diff_max=abs(y-44)
    if diff_min>=diff_max :
        return minn
    elif diff_min<diff_max :
        return maxx
def PC(minn,maxx):
    x=minn
    y=maxx
    diff_min=abs(x-150)
    diff_max=abs(y-450)
    if diff_min>=diff_max :
        return minn
    elif diff_min<diff_max :
        return maxx
def Hemoglobin(minn,maxx):
    x=minn
    y=maxx
    diff_min=abs(x-12.1)
    diff_max=abs(y-17.2)
    if diff_min>=diff_max :
        return minn
    elif diff_min<diff_max :
        return maxx
def BUN(minn,maxx):
    x=minn
    y=maxx
    diff_min=abs(x-7)
    diff_max=abs(y-20)
    if diff_min>=diff_max :
        return minn
    elif diff_min<diff_max :
        return maxx
def Albumin(minn,maxx):
    x=minn
    y=maxx
    diff_min=abs(x-3.5)
    diff_max=abs(y-5.5)
    if diff_min>=diff_max :
        return minn
    elif diff_min<diff_max :
        return maxx
