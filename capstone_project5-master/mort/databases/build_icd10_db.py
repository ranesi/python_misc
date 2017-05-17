import sqlite3

'''
    ICD10 DB Builder
    Purpose: generate an sqlite3 database based on ICD-10 data
    Functions:
        • create_db() -> None
            - create database, define schema
        • icd10_read() -> list
            - read ICD-10 text file sourced from
                https://www.cob.cms.hhs.gov/Section111/help/icd10.dx.codes.htm
        • populate_db(icd_list: list) -> None
            - inserts parsed values into database
        • main() -> None
            - entry point for the program
'''


def create_db():
    """
        Default database name: icd10.db
    """
    schema = '''
    CREATE TABLE icd10(
        code TEXT PRIMARY KEY NOT NULL,
        short_description TEXT NOT NULL,
        long_description TEXT NOT NULL)
    '''

    conn = sqlite3.connect('icd10.db')
    cur = conn.cursor()
    cur.execute(schema)
    conn.commit()
    conn.close()


def icd10_read():
    '''
        NOTE: you must delete the first line of ICD10_DX_Codes.txt
        for this function to work as-is
    '''
    icd_list = []

    with open('ICD10_DX_Codes.txt', 'r') as f:
        for line in f:
            code = line[0:8]
            sd = line[8:70]
            ld = line[70:]
            icd_list.append([code, sd, ld])

    return icd_list


def populate_db(icd_list):

    conn = sqlite3.connect('icd10.db')
    cur = conn.cursor()

    for item in icd_list:
        # parameterization necessary to avoid syntax error
        cur.execute('INSERT INTO icd10 VALUES (?, ?, ?)',
                    (item[0], item[1], item[2]))

    conn.commit()
    conn.close()


def main():
    create_db()
    icd_list = icd10_read()
    populate_db(icd_list)


if __name__ == '__main__':
    main()
