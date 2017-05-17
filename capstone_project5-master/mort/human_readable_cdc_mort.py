import sqlite3
import os
"""
    This file addresses the primary issue with the CDC database:
    being completely unreadable by humans.

    SO the functions here return strings of actual, readable information.

    The code is written in a self-explanitory fashion; the functions themselves
    are presented in on-tape order. That is:

    -resident status
    -education
    -month of death
    -sex
    -age code
    -age
    -place of death
    -marital status
    -work injury
    -manner of death
    -method of disposition
    -autospy
    -activity code
    -icd code
    -race
    -hispanic origin

"""
def readable_death(cdc):
    death = dict(
        id=cdc[0],
        resident_status=get_resident_status(cdc[1]),
        education=get_education(cdc[2]),
        month_of_death=get_month(cdc[3]),
        sex=get_sex(cdc[4]),
        age=get_age(cdc[5], cdc[6]),
        place_of_death=get_place_of_death(cdc[7]),
        marital_status=get_marital_status(cdc[8]),
        work_injury=get_work_injury(cdc[9]),
        manner_of_death=get_manner_of_death(cdc[10]),
        method_of_disposition=get_method_of_disposition(cdc[11]),
        autopsy=get_autospy(cdc[12]),
        cause_of_death=get_cause_of_death(cdc[14]),
        race=get_race(cdc[15]),
        hispanic_origin=get_hispanic_origin(cdc[16])
    )
    return death


def get_resident_status(rs):
    resident_status = {
        '1': 'Resident',
        '2': 'Intra-state/territory nonresident',
        '3': 'Inter-state/territory nonresident',
        '4': 'Foreign resident'
    }
    return resident_status[rs]


def get_education(e):

    # FIRST_GRADE, EIGHTH_GRADE = 1, 8
    # edu_int = int(e)
    # education = {
    #     '00': 'No formal education',
    #     '09': '1 year of high school',
    #     '10': '2 years of high school',
    #     '11': '3 years of high school',
    #     '12': '4 years of high school',
    #     '13': '1 year of college',
    #     '14': '2 years of college',
    #     '15': '3 years of college',
    #     '16': '4 years of college',
    #     '17': '5 or more years of college',
    #     '99': 'Not stated'
    # }
    education = {
        '1': '8th grade or less',
        '2': '9 - 12th grade, no diploma',
        '3': 'High school graduate or GED completed',
        '4': 'Some college credit, but no degree',
        '5': 'Associate degree',
        '6': 'Bachelor\'s degree',
        '7': 'Master\'s degree',
        '8': 'Doctorate or professional degree',
        '9': 'Unknown'
    }
    try:
        return education[e]
    except KeyError:
        return 'Education information not found'
    # if FIRST_GRADE <= edu_int <= EIGHTH_GRADE:
    #     return '{} years of elementary school'.format(edu_int)
    # else:
    #     return education[e.zfill(2)]


def get_month(m):
    months = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }
    return months[m]


def get_sex(s):
    sex = {
        'M': 'Male',
        'F': 'Female'
    }
    return sex[s]


def convert_sex(s):
    sex = {
        'Male': 'M',
        'Female': 'F'
    }
    return sex[s]


def get_age(code, age_str):
    CODE_ENUM = 7
    code_int = int(code) - 1
    ages = ['years', 'months', 'days', 'hours', 'minutes']

    for x in range(CODE_ENUM):
        if code_int == x:
            return '{} {} old'.format(age_str, ages[x])
    return 'Age not stated'


def get_place_of_death(p):
    try:
        place_int = int(p)
        places = [
            'Hospital, clinic, or medical center (inpatient)',
            'Hospital, clinic, or medical center (outpatient/ER)',
            'Hospital, clinic, or medical center (dead on arrival)',
            'Decendent\'s home',
            'Hospice facility',
            'Nursing home or long-term care facility',
            'Other',
            'Place of death unknown'
        ]
        for x in range(len(places) + 1):
            if place_int == x:
                return places[x]
    except ValueError:
        return 'Cannot determine place of death'


def get_marital_status(ms_code):
    ms_codes = {
        'S': 'Never married, single',
        'M': 'Married',
        'W': 'Widowed',
        'D': 'Divorced',
        'U': 'Marital status unknown'
    }
    return ms_codes[ms_code]


def get_work_injury(wi):
    work_injury = {
        'Y': 'Yes',
        'N': 'No',
        'U': 'Unknown'
    }
    return work_injury[wi]


def get_manner_of_death(m):
    manners = [
        'Accident',
        'Suicide',
        'Homicide',
        'Pending investigation',
        'Could not determine',
        'Self-inflicted',
        'Natural'
    ]
    try:
        manner = int(m)
        for x in range(len(manners) + 1):
            if manner == x:
                return manners[x - 1]
    except ValueError:
        return 'Not specified'
    return 'SOMETHING WENT WRONG'


def get_method_of_disposition(m):
    methods = {
        'B': 'Burial',
        'C': 'Cremation',
        'O': 'Other',
        'U': 'Unknown'
    }
    if m in methods.keys():
        return methods[m]
    else:
        return 'Unknown'


def get_autospy(a):
    autopsy = {
        'Y': 'Yes',
        'N': 'No',
        'U': 'Unknown'
    }
    return autopsy[a]


def get_activity(a):
    activities = [
        'While engaged in sports activity',
        'While engaged in leisure activity',
        'While working for income',
        'While engaged in other types of work',
        'While resting, sleeping, or eating (vital activities)',
        'While engaged in other specified activities',
        'During unspecified activity'
    ]
    try:
        act_int = int(a)
        for x in range(len(activities) + 1):
            if act_int == x:
                return activities[x - 1]
    except ValueError:
        return 'Causes other than W00-Y34, except Y06.- and Y07.-'
    return 'SOMETHING WENT WRONG'


def get_cause_of_death(icd_code):
    sql_cmd = '''
    SELECT
        *
    FROM
        icd10
    WHERE
        code LIKE ?
    '''

    try:
        while True:
            if len(icd_code) == 0:
                return 'Invalid ICD-10 Code Supplied'
            else:
                conn = sqlite3.connect(os.path.join('databases/icd10.db'))
                conn.row_factory = sqlite3.Row
                cur = conn.execute(sql_cmd, ['%' + icd_code + '%'])
                query = cur.fetchone()
                if query is not None:
                    ret = query[2]  # long description of condition
                    conn.close()
                    return ret
                else:
                    icd_code = icd_code[:-1]
                conn.close()
    except sqlite3.Error:
        return 'Error connecting to database'


def get_race(r):
    races = {
        '01': 'White',
        '02': 'Black',
        '03': 'Amerindian (including Aleut and Eskimo)',
        '04': 'Chinese',
        '05': 'Japanese',
        '06': 'Hawaiian',
        '07': 'Filipino',
        '18': 'Asian Indian',
        '28': 'Korean',
        '38': 'Samoan',
        '48': 'Vietnamese',
        '58': 'Guamanian',
        '68': 'Other Asian or Pacific Islander',
        '78': 'Combined other Asian or Pacific Islander'
    }
    return races[r]


def get_race_by_name(r):
    r = r.title()
    races = {
        'White': '01',
        'Black': '02',
        'Amerindian (including Aleut and Eskimo)': '03',
        'Chinese': '04',
        'Japanese': '05',
        'Hawaiian': '06',
        'Filipino': '07',
        'Asian Indian': '18',
        'Korean': '28',
        'Samoan': '38',
        'Vietnamese': '48',
        'Guamanian': '49',
        'Other Asian or Pacific Islander': '68',
        'Combined other Asian or Pacific Islander': '78'
    }
    try:
        races[r]
    except KeyError:
        return '68'
    else:
        return races[r]


def get_hispanic_origin(h):
    try:
        h_int = int(h)
        if 100 <= h_int <= 199:
            return 'Non-Hispanic'
        elif 200 <= h_int <= 209:
            return 'Spaniard'
        elif 210 <= h_int <= 219:
            return 'Mexican'
        elif 260 <= h_int <= 269:
            return 'Puerto Rican'
        elif 270 <= h_int <= 274:
            return 'Cuban'
        elif 275 <= h_int <= 279:
            return 'Dominican'
        elif 221 <= h_int <= 230:
            return 'Central American'
        elif 231 <= h_int <= 249:
            return 'South American'
        elif 250 <= h_int <= 259:
            return 'Latin American'
        elif 280 <= h_int <= 299:
            return 'Other Hispanic'
        elif h_int == 220:
            return 'Central and South American'
        else:
            return 'Unknown'
    except ValueError:
        return 'Unknown'
