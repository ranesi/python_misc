# CDC 2015 Mortality Visualizer  
To run:  
==============================  
-`pip` and `export FLASK_APP=mort` or  
-just `export FLASK_APP=mort.py` in `mort/`  

Setup:
=============================  
-download VS15MORT.DUSMCPUB from the CDC [here](http://www.nber.org/mortality/ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/DVS/mortality/)  
-download `ICD10_DX_Codes.txt` [here](https://www.cob.cms.hhs.gov/Section111/help/icd10.dx.codes.htm)  
-extract both entries to `/mort/databases/`  
-`cd` to `/databases`, then `python build_cdc_mortality.db` and `python build_icd10_db.py`
