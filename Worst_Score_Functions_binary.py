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
	if (minn <= 80 or maxx >= 100):
		return 1
	else:
		return 0
    
def Temperature(minn,maxx):
	if (minn <= 36 or maxx >= 38.4):
		return 1
	else:
		return 0

def HeartRate(minn,maxx):
	if (minn <= 70 or maxx >= 100):
		return 1
	else:
		return 0

def MAP(minn,maxx):
	if (minn <= 70 or maxx >= 109):
		return 1
	else:
		return 0

def RR(minn,maxx):
	if (minn <= 12 or maxx >= 24):
		return 1
	else:
		return 0

def ArterialpH(minn,maxx):
	if (minn <= 7.33 or maxx >= 7.49):
		return 1
	else:
		return 0

def Sodium(minn,maxx):
	if (minn <= 130 or maxx >= 149):
		return 1
	else:
		return 0

def Potassium(minn,maxx):
	if (minn <= 3.5 or maxx >= 5.4):
		return 1
	else:
		return 0

def Creatinine(minn,maxx):
	if (minn <= 0.6 or maxx >= 1.4):
		return 1
	else:
		return 0

def Hematocrit(minn,maxx):
	if (minn <= 30 or maxx >= 45.9):
		return 1
	else:
		return 0

def WBC(minn,maxx):
	if (minn <= 3 or maxx >= 14.9):
		return 1
	else:
		return 0

def HCO3(minn,maxx):
	if (minn <= 22 or maxx >= 31.9):
		return 1
	else:
		return 0

def PC(minn,maxx):
	if (minn <= 150 or maxx >= 450):
		return 1
	else:
		return 0

def Hemoglobin(minn,maxx):
	if (minn <= 12.1 or maxx >= 17.2):
		return 1
	else:
		return 0

def BUN(minn,maxx):
	if (minn <= 7 or maxx >= 20):
		return 1
	else:
		return 0

def Albumin(minn,maxx):
	if (minn <= 3.5 or maxx >= 5.5):
		return 1
	else:
		return 0
