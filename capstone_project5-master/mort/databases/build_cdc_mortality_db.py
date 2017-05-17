import csv
import sqlite3
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from tables import CDCEntry
"""
    CDC Mortality DB Builder
    Purpose: program to convert the CDC's morbidity/mortality file to
             an SQLite3 database
             File found at:
             http://www.nber.org/mortality/ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/DVS/mortality/
    Functions:
        • create_db() -> None
            - create database, table, define table schema
        • read_cdc_file() -> list
            - parses VS15MORT.DUSMCPUB
            - returns list of entries
    • populate_cdc_db(cdc_list: list) -> None

            - generates SQLite3 database from list
        • main() -> None
            - entry point of program
"""


def create_db():

    init = '''
DROP TABLE IF EXISTS cdc_mortality
    '''
    schema = '''
CREATE TABLE cdc_mortality(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    resident_status TEXT,
    education TEXT,
    month_of_death TEXT,
    sex TEXT,
    age_code TEXT,
    age TEXT,
    place_of_death TEXT,
    marital_status TEXT,
    work_injury TEXT,
    manner_of_death TEXT,
    method_of_disposition TEXT,
    autopsy TEXT,
    activity_code TEXT,
    icd_code TEXT,
    race TEXT,
    hispanic_origin TEXT
)
    '''

    conn = sqlite3.connect('cdc_mortality.db')
    cur = conn.cursor()
    cur.execute(init)
    cur.execute(schema)
    conn.commit()
    conn.close()

# NOTE: The following function is (very) loosely based
# on the inexplicable VS15MORT.DUSMCPUB-to-CSV parser
# found at the following URL:
# https://github.com/tommaho/VS13MORT.DUSMCPUB-Parser


def read_cdc_file():

    cdc_data = []

    with open('VS15MORT.DUSMCPUB', 'r') as f:
        for line in f:
            resident_status = line[19].strip()
            education = line[62].strip()
            month_of_death = line[64:67].strip()
            sex = line[68].strip()
            age_code = line[69].strip()
            age = line[70:73].strip()
            place_of_death = line[82].strip()
            marital_status = line[83].strip()
            work_injury = line[105].strip()
            manner_of_death = line[106].strip()
            method_of_disposition = line[107].strip()
            autopsy = line[108].strip()
            activity_code = line[143].strip()
            icd_code = line[145:149].strip()
            race = line[444:446].strip()
            hispanic_origin = line[483:486].strip()

            cdc_data.append([
                resident_status,
                education,
                month_of_death,
                sex,
                age_code,
                age,
                place_of_death,
                marital_status,
                work_injury,
                manner_of_death,
                method_of_disposition,
                autopsy,
                activity_code,
                icd_code,
                race,
                hispanic_origin,
            ])

    return cdc_data

# def populate_sa_cdc_db(cdc_list):
#     for c in cdc_list:
#         db.session.add(
#             CDCEntry(
#                 resident_status=c[0],
#                 education=c[1],
#                 month_of_death=c[2],
#                 sex=c[3],
#                 age_code=c[4],
#                 age=c[5],
#                 place_of_death=c[6],
#                 marital_status=c[7],
#                 work_injury=c[8],
#                 manner_of_death=c[9],
#                 method_of_disposition=c[10],
#                 autopsy=c[11],
#                 activity_code=c[12],
#                 icd_code=c[13],
#                 race=c[14],
#                 hispanic_origin=c[15]
#             )
#         )
#     db.session.commit()
#     db.session.close()


def populate_sl3_cdc_db(cdc_list):

    cmd = '''
INSERT INTO cdc_mortality (
    resident_status,
    education,
    month_of_death,
    sex,
    age_code,
    age,
    place_of_death,
    marital_status,
    work_injury,
    manner_of_death,
    method_of_disposition,
    autopsy,
    activity_code,
    icd_code,
    race,
    hispanic_origin
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    conn = sqlite3.connect('cdc_mortality.db')
    cur = conn.cursor()
    for c in cdc_list:
        cur.execute(
            cmd,
            (c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7],
             c[8], c[9], c[10], c[11], c[12], c[13], c[14], c[15])
        )
    conn.commit()
    conn.close()


def main():
    create_db()
    cdc_data = read_cdc_file()
    populate_sl3_cdc_db(cdc_data)
    # populate_sa_cdc_db(cdc_data)


if __name__ == '__main__':
    main()
