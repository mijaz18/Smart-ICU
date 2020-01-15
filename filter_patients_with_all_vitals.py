import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
mimic_db = create_engine("mysql+mysqldb://mimic:"+'mimic'+"@adcom.mmzzhh.com/mimic_filtered_a")

df_arterial_ph = pd.read_sql("SELECT * FROM arterial_ph_IDS", con=mimic_db)
#df_arterial_bp = pd.read_sql("SELECT * FROM art_bp_mean_IDS", con=mimic_db)
df_creatinine = pd.read_sql("SELECT * FROM creatinine_IDS", con=mimic_db)
df_gcs_e = pd.read_sql("SELECT * FROM gcs_eye_IDS", con=mimic_db)
df_gcs_m = pd.read_sql("SELECT * FROM gcs_motor_IDS", con=mimic_db)
df_gcs_v = pd.read_sql("SELECT * FROM gcs_verbal_IDS", con=mimic_db)
df_hco3 = pd.read_sql("SELECT * FROM hco3_IDS", con=mimic_db)
df_hr = pd.read_sql("SELECT * FROM heart_rate_IDS", con=mimic_db)
df_hematocrit = pd.read_sql("SELECT * FROM hematocrit_IDS", con=mimic_db)
df_pottasium = pd.read_sql("SELECT * FROM pottasium_IDS", con=mimic_db)
df_respiratory = pd.read_sql("SELECT * FROM respiratory_IDS", con=mimic_db)
df_sodium = pd.read_sql("SELECT * FROM sodium_IDS", con=mimic_db)
df_temp = pd.read_sql("SELECT * FROM temperature_IDS", con=mimic_db)
df_wbc = pd.read_sql("SELECT * FROM wbc_IDS", con=mimic_db)

## New vitals
df_plateC = pd.read_sql("SELECT * FROM plate_count_IDS", con=mimic_db)
df_hemoglubin = pd.read_sql("SELECT * FROM hemoglubin_IDS", con=mimic_db)
df_bun = pd.read_sql("SELECT * FROM bun_IDS", con=mimic_db)
df_po2 = pd.read_sql("SELECT * FROM PO2_IDS", con=mimic_db)

df_list = [df_po2, df_arterial_ph, df_bun, df_hemoglubin, df_plateC, df_gcs_e, df_gcs_m, df_gcs_v, df_hco3, df_hr, df_hematocrit, df_pottasium, df_respiratory, df_sodium, df_temp, df_wbc]
           
df = df_list[0]
for df_ in  df_list[1:]:
    df = df.merge(df_, on='subject_ids')
    
#merge_data = pd.merge(df_gcs, df_arterial_bp, on='subject_ids');
#                      df_gcs,df_hco3,df_hr,
#                      df_hematocrit,df_pottasium,df_respiratory,df_sodium,df_temp,df_wbc, on='subject_ids')

df.to_sql('filtered_subjects', con=mimic_db)
