DROP TABLE IF EXISTS cdc_mortality;


CREATE TABLE cdc_mortality( id INTEGER PRIMARY KEY AUTOINCREMENT, resident_status TEXT, education TEXT, month_of_death TEXT, sex TEXT, age_code TEXT, age TEXT, place_of_death TEXT, marital_status TEXT, work_injury TEXT, manner_of_death TEXT, method_of_disposition TEXT, autopsy TEXT, activity_code TEXT, icd_code TEXT, race TEXT, hispanic_origin TEXT);
