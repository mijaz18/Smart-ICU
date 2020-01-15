drop table if exists heart_rate_IDS;
create table mimic_filtered_c.heart_rate_IDS (subject_ids int);
insert into mimic_filtered_c.heart_rate_IDS
SELECT SUBJECT_ID FROM mimic_jth.CHARTEVENTS WHERE ITEMID = 220045
Group by subject_id;

drop table if exists gcs_eye_IDS;
create table mimic_filtered_c.gcs_eye_IDS (subject_ids int);
insert into mimic_filtered_c.gcs_eye_IDS
SELECT SUBJECT_ID FROM mimic_jth.CHARTEVENTS WHERE ITEMID = 220739
Group by subject_id;

drop table if exists gcs_motor_IDS;
create table mimic_filtered_c.gcs_motor_IDS (subject_ids int);
insert into mimic_filtered_c.gcs_motor_IDS
SELECT SUBJECT_ID FROM mimic_jth.CHARTEVENTS WHERE ITEMID = 223901
Group by subject_id;

drop table if exists gcs_verbal_IDS;
create table mimic_filtered_c.gcs_verbal_IDS (subject_ids int);
insert into mimic_filtered_c.gcs_verbal_IDS
SELECT SUBJECT_ID FROM mimic_jth.CHARTEVENTS WHERE ITEMID = 223900
Group by subject_id;


drop table if exists temperature_IDS;
create table mimic_filtered_c.temperature_IDS (subject_ids int);
insert into mimic_filtered_c.temperature_IDS
SELECT SUBJECT_ID FROM mimic_jth.CHARTEVENTS WHERE ITEMID = 223761
Group by subject_id;

drop table if exists art_bp_mean_IDS;
create table mimic_filtered_c.art_bp_mean_IDS (subject_ids int);
insert into mimic_filtered_c.art_bp_mean_IDS
SELECT SUBJECT_ID FROM mimic_jth.CHARTEVENTS WHERE ITEMID = 220052
Group by subject_id;

/* drop table if exists art_bp_mean_a_IDS;
create table mimic_filtered_c.art_bp_mean_a_IDS (subject_ids int);
insert into mimic_filtered_c.art_bp_mean_a_IDS
SELECT SUBJECT_ID FROM mimic_jth.CHARTEVENTS WHERE ITEMID = 220052
Group by subject_id;

drop table if exists art_bp_mean_b_IDS;
create table mimic_filtered_c.art_bp_mean_b_IDS (subject_ids int);
insert into mimic_filtered_c.art_bp_mean_b_IDS
SELECT SUBJECT_ID FROM mimic_jth.CHARTEVENTS WHERE ITEMID = 225312
Group by subject_id; */

drop table if exists respiratory_IDS;
create table mimic_filtered_c.respiratory_IDS (subject_ids int);
insert into mimic_filtered_c.respiratory_IDS
SELECT SUBJECT_ID FROM mimic_jth.CHARTEVENTS WHERE ITEMID = 220210
Group by subject_id;

drop table if exists arterial_ph_IDS;
create table mimic_filtered_c.arterial_ph_IDS (subject_ids int);
insert into mimic_filtered_c.arterial_ph_IDS
SELECT SUBJECT_ID FROM mimic_jth.LABEVENTS WHERE ITEMID = 50820
Group by subject_id;


drop table if exists sodium_IDS;
create table mimic_filtered_c.sodium_IDS (subject_ids int);
insert into mimic_filtered_c.sodium_IDS
SELECT SUBJECT_ID FROM mimic_jth.LABEVENTS WHERE ITEMID = 50983
Group by subject_id;

drop table if exists pottasium_IDS;
create table mimic_filtered_c.pottasium_IDS (subject_ids int);
insert into mimic_filtered_c.pottasium_IDS
SELECT SUBJECT_ID FROM mimic_jth.LABEVENTS WHERE ITEMID = 50971
Group by subject_id;

drop table if exists creatinine_IDS;
create table mimic_filtered_c.creatinine_IDS (subject_ids int);
insert into mimic_filtered_c.creatinine_IDS
SELECT SUBJECT_ID FROM mimic_jth.LABEVENTS WHERE ITEMID = 50912
Group by subject_id;

drop table if exists hematocrit_IDS;
create table mimic_filtered_c.hematocrit_IDS (subject_ids int);
insert into mimic_filtered_c.hematocrit_IDS
SELECT SUBJECT_ID FROM mimic_jth.LABEVENTS WHERE ITEMID = 51221
Group by subject_id;

drop table if exists wbc_IDS;
create table mimic_filtered_c.wbc_IDS (subject_ids int);
insert into mimic_filtered_c.wbc_IDS
SELECT SUBJECT_ID FROM mimic_jth.CHARTEVENTS WHERE ITEMID = 220546
Group by subject_id;

drop table if exists hco3_IDS;
create table mimic_filtered_c.hco3_IDS (subject_ids int);
insert into mimic_filtered_c.hco3_IDS
SELECT SUBJECT_ID FROM mimic_jth.LABEVENTS WHERE ITEMID = 50882
Group by subject_id;

