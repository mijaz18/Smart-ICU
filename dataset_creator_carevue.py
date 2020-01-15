# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:34:41 2018
For carevue database
@author: zulqarnain
"""

#import os
#os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

import time
import Worst_Score_Functions_binary as sc
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector
import datetime as dt
from sqlalchemy import create_engine

mimic_db_filter = create_engine("mysql+mysqldb://mimic:"+'mimic'+"@adcom.mmzzhh.com/mimic_filtered_care_b")
mimic_db_th = create_engine("mysql+mysqldb://mimic:"+'mimic'+"@adcom.mmzzhh.com/mimic_5_care_b")



df_patients = pd.read_sql("SELECT subject_ids from filtered_subjects", con=mimic_db_filter)

df_patients['Heart_Rate_Score'] = 0
df_patients['SPO2'] = 0
df_patients['Mean_Arterial_Pressure'] = 0
df_patients['Mean_Arterial_pH'] = 0
df_patients['Temperature'] = 0
df_patients['Repsiratory_Rate'] = 0
df_patients['Serum_Sodium'] = 0
df_patients['Serum_Potassium'] = 0
df_patients['Serum_Creatinine'] = 0
df_patients['Hematocrit'] = 0
df_patients['White_Blood_Cells'] = 0
df_patients['Platelet_Count'] = 0
df_patients['Hemoglubin'] = 0
df_patients['BUN'] = 0
df_patients['GCS'] = 0
df_patients['Serum_HCO3'] = 0
df_patients['AGE'] = 0
df_patients['Admission_Type'] = 0
df_patients['Expiry_Status'] = 0

## Fetch Data from Database for Age and Expiry and Admission Type. Make sure the table Patients_Age exist
df_age_exp_all = pd.read_sql("SELECT SUBJECT_ID, AGE, EXPIRE_FLAG FROM PATIENTS_AGE", con=mimic_db_th)
df_age_exp_all.set_index("SUBJECT_ID", inplace=True)

df_admit_type_all = pd.read_sql("SELECT SUBJECT_ID, ADMISSION_TYPE FROM PATIENTS_AGE", con=mimic_db_th)
df_admit_type_all.set_index("SUBJECT_ID", inplace=True)

## Fetch Data from Database against all vitals for CHARTEVENTS
df_hr_all = pd.read_sql("SELECT ROW_ID, SUBJECT_ID, CHARTTIME, VALUENUM FROM CHARTEVENTS WHERE ITEMID=211 ORDER BY ROW_ID ASC", con=mimic_db_th)
df_hr_all.set_index("SUBJECT_ID", inplace=True)

df_temp_all = pd.read_sql("SELECT ROW_ID, SUBJECT_ID, CHARTTIME, VALUENUM FROM CHARTEVENTS WHERE ITEMID=678 ORDER BY ROW_ID ASC", con=mimic_db_th)
df_temp_all.set_index("SUBJECT_ID", inplace=True)

df_resp_all = pd.read_sql("SELECT ROW_ID, SUBJECT_ID, CHARTTIME, VALUENUM FROM CHARTEVENTS WHERE ITEMID=618 ORDER BY ROW_ID ASC", con=mimic_db_th)
df_resp_all.set_index("SUBJECT_ID", inplace=True)

df_wbc_all = pd.read_sql("SELECT ROW_ID, SUBJECT_ID, CHARTTIME, VALUENUM FROM CHARTEVENTS WHERE ITEMID=1542 ORDER BY ROW_ID ASC", con=mimic_db_th)
df_wbc_all.set_index("SUBJECT_ID", inplace=True)

df_gcs_all = pd.read_sql("SELECT ROW_ID, SUBJECT_ID, CHARTTIME, VALUENUM FROM CHARTEVENTS WHERE ITEMID=198 ORDER BY ROW_ID ASC", con=mimic_db_th)
df_gcs_all.set_index("SUBJECT_ID", inplace=True)


## Additional vitals
df_plate_count_all = pd.read_sql("SELECT ROW_ID, SUBJECT_ID, CHARTTIME, VALUENUM FROM CHARTEVENTS WHERE ITEMID=828 ORDER BY ROW_ID ASC", con=mimic_db_th)
df_plate_count_all.set_index("SUBJECT_ID", inplace=True)

df_hemoglubin_all = pd.read_sql("SELECT ROW_ID, SUBJECT_ID, CHARTTIME, VALUENUM FROM CHARTEVENTS WHERE ITEMID=814 ORDER BY ROW_ID ASC", con=mimic_db_th)
df_hemoglubin_all.set_index("SUBJECT_ID", inplace=True)

df_bun_all = pd.read_sql("SELECT ROW_ID, SUBJECT_ID, CHARTTIME, VALUENUM FROM CHARTEVENTS WHERE ITEMID=781 ORDER BY ROW_ID ASC", con=mimic_db_th)
df_bun_all.set_index("SUBJECT_ID", inplace=True)


df_map_all = pd.read_sql("SELECT ROW_ID, SUBJECT_ID, CHARTTIME, VALUENUM FROM CHARTEVENTS WHERE ITEMID=52 ORDER BY ROW_ID ASC", con=mimic_db_th)
df_map_all.set_index("SUBJECT_ID", inplace=True)


#### For LAB Events Vitals
df_art_ph_all = pd.read_sql("SELECT ROW_ID, SUBJECT_ID, CHARTTIME, VALUENUM FROM CHARTEVENTS WHERE ITEMID=780 ORDER BY ROW_ID ASC", con=mimic_db_th)
df_art_ph_all.set_index("SUBJECT_ID", inplace=True)

df_sodium_all = pd.read_sql("SELECT ROW_ID, SUBJECT_ID, CHARTTIME, VALUENUM FROM CHARTEVENTS WHERE ITEMID=1536 ORDER BY ROW_ID ASC", con=mimic_db_th)
df_sodium_all.set_index("SUBJECT_ID", inplace=True)

df_potassium_all = pd.read_sql("SELECT ROW_ID, SUBJECT_ID, CHARTTIME, VALUENUM FROM CHARTEVENTS WHERE ITEMID=1535 ORDER BY ROW_ID ASC", con=mimic_db_th)
df_potassium_all.set_index("SUBJECT_ID", inplace=True)

df_creatinine_all = pd.read_sql("SELECT ROW_ID, SUBJECT_ID, CHARTTIME, VALUENUM FROM CHARTEVENTS WHERE ITEMID=1525 ORDER BY ROW_ID ASC", con=mimic_db_th)
df_creatinine_all.set_index("SUBJECT_ID", inplace=True)

df_hematocrit_all = pd.read_sql("SELECT ROW_ID, SUBJECT_ID, CHARTTIME, VALUENUM FROM CHARTEVENTS WHERE ITEMID=813 ORDER BY ROW_ID ASC", con=mimic_db_th)
df_hematocrit_all.set_index("SUBJECT_ID", inplace=True)

df_hco3_all = pd.read_sql("SELECT ROW_ID, SUBJECT_ID, CHARTTIME, VALUENUM FROM LABEVENTS WHERE ITEMID=50882 ORDER BY ROW_ID ASC", con=mimic_db_th)
df_hco3_all.set_index("SUBJECT_ID", inplace=True)

df_spo2_all = pd.read_sql("SELECT ROW_ID, SUBJECT_ID, CHARTTIME, VALUENUM FROM CHARTEVENTS WHERE ITEMID=646 ORDER BY ROW_ID ASC", con=mimic_db_th)
df_spo2_all.set_index("SUBJECT_ID", inplace=True)


## Super fast loop. data stored in RAM for super fetching
#def parloops(patient_len):
#df_pat = df_patients.copy()
start_time = time.time()
index = 0;
while index < len(df_patients):
#for index in range(0,len(df_patients)):
    print ("Current index is: ", index)
    patient_id = df_patients.subject_ids.iloc[index]
    ## Fetch data of age and expire status
    df_age_exp = df_age_exp_all.loc[[patient_id]]
    age = df_age_exp['AGE'].values
    expiry_flag = df_age_exp['EXPIRE_FLAG'].values
    df_admit_type = df_admit_type_all.loc[[patient_id]]
    admit_type = df_admit_type.iloc[:,0].values.astype(str)
    ## Assign Points according to admission Type
    if (admit_type == 'EMERGENCY'):
        admit_type = 5;
    elif (admit_type == 'ELECTIVE'):
        admit_type = 2;
    elif(admit_type == 'URGENT'):
        admit_type = 6;
    else:
        admit_type = 1
    
    ### Chartevents Vitals
    df_hr = pd.DataFrame(df_hr_all.loc[[patient_id]])
    df_hr = df_hr[np.isfinite(df_hr['VALUENUM'])]
    if (df_hr.empty):
        index = index + 1;
        continue;
    df_temp = pd.DataFrame(df_temp_all.loc[[patient_id]])
    df_temp = df_temp[np.isfinite(df_temp['VALUENUM'])]
    if (df_temp.empty):
        index = index + 1;
        continue;
    df_resp = pd.DataFrame(df_resp_all.loc[[patient_id]])
    df_resp = df_resp[np.isfinite(df_resp['VALUENUM'])]
    if (df_resp.empty):
        index = index + 1;
        continue;
    df_wbc = pd.DataFrame(df_wbc_all.loc[[patient_id]])
    df_wbc = df_wbc[np.isfinite(df_wbc['VALUENUM'])]
    if (df_wbc.empty):
        index = index + 1;
        continue;
    df_gcs = pd.DataFrame(df_gcs_all.loc[[patient_id]])
    df_gcs = df_gcs[np.isfinite(df_gcs['VALUENUM'])]
    if (df_gcs.empty):
        index = index + 1;
        continue;
    df_plate_count = pd.DataFrame(df_plate_count_all.loc[[patient_id]])
    df_plate_count = df_plate_count[np.isfinite(df_plate_count['VALUENUM'])]
    if (df_plate_count.empty):
        index = index + 1;
        continue;
    df_hemoglubin = pd.DataFrame(df_hemoglubin_all.loc[[patient_id]])
    df_hemoglubin = df_hemoglubin[np.isfinite(df_hemoglubin['VALUENUM'])]
    if (df_hemoglubin.empty):
        index = index + 1;
        continue;
    df_bun = pd.DataFrame(df_bun_all.loc[[patient_id]])
    df_bun = df_bun[np.isfinite(df_bun['VALUENUM'])]
    if (df_bun.empty):
        index = index + 1;
        continue;
    df_map = pd.DataFrame(df_map_all.loc[[patient_id]])    
    df_map = df_map[np.isfinite(df_map['VALUENUM'])]
    if (df_map.empty):
        index = index + 1;
        continue;
    ### LAB events Vitals
    df_art_ph = pd.DataFrame(df_art_ph_all.loc[[patient_id]])
    df_art_ph = df_art_ph[np.isfinite(df_art_ph['VALUENUM'])]
    if (df_art_ph.empty):
        index = index + 1;
        continue;
    df_sodium = pd.DataFrame(df_sodium_all.loc[[patient_id]])
    df_sodium = df_sodium[np.isfinite(df_sodium['VALUENUM'])]
    if (df_sodium.empty):
        index = index + 1;
        continue;
    df_potassium = pd.DataFrame(df_potassium_all.loc[[patient_id]])
    df_potassium = df_potassium[np.isfinite(df_potassium['VALUENUM'])]
    if (df_potassium.empty):
        index = index + 1;
        continue;
    df_creatinine = pd.DataFrame(df_creatinine_all.loc[[patient_id]])
    df_creatinine = df_creatinine[np.isfinite(df_creatinine['VALUENUM'])]
    if (df_creatinine.empty):
        index = index + 1;
        continue;
    df_hematocrit = pd.DataFrame(df_hematocrit_all.loc[[patient_id]])    
    df_hematocrit = df_hematocrit[np.isfinite(df_hematocrit['VALUENUM'])]
    if (df_hematocrit.empty):
        index = index + 1;
        continue;
    df_hco3 = pd.DataFrame(df_hco3_all.loc[[patient_id]])  
    df_hco3 = df_hco3[np.isfinite(df_hco3['VALUENUM'])]
    if (df_hco3.empty):
        index = index + 1;
        continue;
    df_spo2 = pd.DataFrame(df_spo2_all.loc[[patient_id]])  
    df_spo2 = df_spo2[np.isfinite(df_spo2['VALUENUM'])]        
    if (df_spo2.empty):
        index = index + 1;
        continue;
    ### Chartevents Vitals
    df_temp.reset_index(inplace=True)
    df_hr.reset_index(inplace=True)
    df_resp.reset_index(inplace=True)
    df_wbc.reset_index(inplace=True)
    df_gcs.reset_index(inplace=True)
    df_plate_count.reset_index(inplace=True)
    df_hemoglubin.reset_index(inplace=True)
    df_bun.reset_index(inplace=True)
    df_map.reset_index(inplace=True)
    ### LAB events Vitals
    df_art_ph.reset_index(inplace=True)
    df_sodium.reset_index(inplace=True)
    df_potassium.reset_index(inplace=True)
    df_creatinine.reset_index(inplace=True)
    df_hematocrit.reset_index(inplace=True)
    df_hco3.reset_index(inplace=True) 
    df_spo2.reset_index(inplace=True)
        
    ### Chartevents Vitals
    x_hr = df_hr[df_hr['CHARTTIME']<=(df_hr.CHARTTIME[0]+dt.timedelta(days=1))]['VALUENUM']
    x_temp = df_temp[df_temp['CHARTTIME']<=(df_temp.CHARTTIME[0]+dt.timedelta(days=1))]['VALUENUM']
    x_resp = df_resp[df_resp['CHARTTIME']<=(df_resp.CHARTTIME[0]+dt.timedelta(days=1))]['VALUENUM']
    x_wbc = df_wbc[df_wbc['CHARTTIME']<=(df_wbc.CHARTTIME[0]+dt.timedelta(days=1))]['VALUENUM']
    x_gcs = df_gcs[df_gcs['CHARTTIME']<=(df_gcs.CHARTTIME[0]+dt.timedelta(days=1))]['VALUENUM']
    x_plate_count = df_plate_count[df_plate_count['CHARTTIME']<=(df_plate_count.CHARTTIME[0]+dt.timedelta(days=1))]['VALUENUM']
    x_hemoglubin = df_hemoglubin[df_hemoglubin['CHARTTIME']<=(df_hemoglubin.CHARTTIME[0]+dt.timedelta(days=1))]['VALUENUM']
    x_bun = df_bun[df_bun['CHARTTIME']<=(df_bun.CHARTTIME[0]+dt.timedelta(days=1))]['VALUENUM']
    x_map = df_map[df_map['CHARTTIME']<=(df_map.CHARTTIME[0]+dt.timedelta(days=1))]['VALUENUM']
    ### LAB events Vitals
    x_art_ph = df_art_ph[df_art_ph['CHARTTIME']<=(df_art_ph.CHARTTIME[0]+dt.timedelta(days=1))]['VALUENUM']
    x_sodium = df_sodium[df_sodium['CHARTTIME']<=(df_sodium.CHARTTIME[0]+dt.timedelta(days=1))]['VALUENUM']
    x_potassium = df_potassium[df_potassium['CHARTTIME']<=(df_potassium.CHARTTIME[0]+dt.timedelta(days=1))]['VALUENUM']
    x_creatinine = df_creatinine[df_creatinine['CHARTTIME']<=(df_creatinine.CHARTTIME[0]+dt.timedelta(days=1))]['VALUENUM']
    x_hematocrit = df_hematocrit[df_hematocrit['CHARTTIME']<=(df_hematocrit.CHARTTIME[0]+dt.timedelta(days=1))]['VALUENUM']
    x_hco3 = df_hco3[df_hco3['CHARTTIME']<=(df_hco3.CHARTTIME[0]+dt.timedelta(days=1))]['VALUENUM']
    x_spo2 = df_spo2[df_spo2['CHARTTIME']<=(df_spo2.CHARTTIME[0]+dt.timedelta(days=1))]['VALUENUM']
    
    ### Chartevents Vitals    
    x_hr = pd.to_numeric(x_hr)
    x_temp = round((((pd.to_numeric(x_temp))-32)*(5/9)),1)
    x_resp = pd.to_numeric(x_resp)
    x_wbc = pd.to_numeric(x_wbc)
    x_gcs = pd.to_numeric(x_gcs)
    x_plate_count = pd.to_numeric(x_plate_count)
    x_hemoglubin = pd.to_numeric(x_hemoglubin)
    x_bun = pd.to_numeric(x_bun)
#    x_map = pd.to_numeric(x_map)
    ### LAB events Vitals
#    x_art_ph = pd.to_numeric(x_art_ph)
    x_sodium = pd.to_numeric(x_sodium)
    x_potassium = pd.to_numeric(x_potassium)
    x_creatinine = pd.to_numeric(x_creatinine)
    x_hematocrit = pd.to_numeric(x_hematocrit)
    x_hco3 = pd.to_numeric(x_hco3)
    x_spo2 = pd.to_numeric(x_spo2)
    
    ### Chartevents Vitals  
    df_patients.Heart_Rate_Score.iloc[index] = sc.HeartRate(min(x_hr),max(x_hr));    
    df_patients.Temperature.iloc[index] = sc.Temperature(min(x_temp),max(x_temp));
    df_patients.Repsiratory_Rate.iloc[index] = sc.RR(min(x_resp),max(x_resp));
    df_patients.White_Blood_Cells.iloc[index] = sc.WBC(min(x_wbc),max(x_wbc));
    df_patients.Platelet_Count.iloc[index] = sc.PC(min(x_plate_count),max(x_plate_count));
    df_patients.Hemoglubin.iloc[index] = sc.Hemoglobin(min(x_hemoglubin),max(x_hemoglubin));
    df_patients.BUN.iloc[index] = sc.BUN(min(x_bun),max(x_bun));
    df_patients.GCS.iloc[index] = 15-min(x_gcs);
    df_patients.Serum_Sodium.iloc[index] = sc.Sodium(min(x_sodium),max(x_sodium));
    df_patients.Serum_Potassium.iloc[index] = sc.Potassium(min(x_potassium),max(x_potassium));
    df_patients.Serum_Creatinine.iloc[index] = sc.Creatinine(min(x_creatinine),max(x_creatinine));        
    df_patients.Hematocrit.iloc[index] = sc.Hematocrit(min(x_hematocrit),max(x_hematocrit));            
    df_patients.Serum_HCO3.iloc[index] = sc.HCO3(min(x_hco3),max(x_hco3));
    df_patients.Mean_Arterial_Pressure.iloc[index] = sc.MAP(min(x_map), max(x_map));
    df_patients.Mean_Arterial_pH.iloc[index] = sc.ArterialpH(min(x_art_ph), max(x_art_ph));
    df_patients.SPO2.iloc[index] = min(x_spo2);
    ## Add data of age and expiry
    df_patients.AGE.iloc[index] = sc.Age(age);
    df_patients.Expiry_Status.iloc[index] =  expiry_flag;
    df_patients.Admission_Type.iloc[index] =  admit_type;   
    index = index + 1;
df_patients = df_patients[df_patients.AGE != 0]
#    return df_pat
df_patients.to_csv('df_patients_care_b.csv')
#import multiprocessing as mp 
### Time counter for loop execution
#
#start_time = time.time()
#
#if __name__ == '__main__':
#
#
#    ranges = [
#        range(0, 600),
#        range(600, 1200),
#        range(1200, 1800),
#        range(1800, 2400),
#        range(2400, 3000),
#        range(3000, 3330)
#    ]
#
## Create a threadpool with N threads
#    pool = mp.Pool(6)
#    result = pool.map(parloops, ranges)
#    pool.close()
#    pool.join()
#    df = pd.concat(result, axis=0)
#    df.to_csv('df_patients_mimic_eth.csv')
print("--- %s seconds ---" % (time.time() - start_time))
#df = pd.read_csv("df_patients_mimic_eth.csv")
#df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
#df.set_index("subject_ids", inplace=True)
#
#df = df[(df.T != 0).any()]
#df.to_csv('df_patients_mimic_eth.csv')
