import sqlite3
import os
from human_readable_cdc_mort import get_cause_of_death as cod
from human_readable_cdc_mort import get_race_by_name as gr
from human_readable_cdc_mort import convert_sex as cs

sql_files = dict(
    cod_query='top10.sql',
    age_query='by_age.sql',
    race_query='by_race.sql',
    random_query='random.sql',
    detailed='user_specified.sql'
)

DIR_PATH = 'databases/queries/'

'''
    CDC Querying Module
    Purpose:
        • Read CDC database
        • Prepare CDC results to be served
    Functions:
        • get_sql_file(cmd: str) -> str
            - open and retrieve applicable SQL query
        • connect_db(query: str, value: str) -> sqlite3.row
            - uses query/value to return results from database
        • build_dict(query: sqlite3.Row) -> list(dict)
            - converts sqlite3 row object to a list containing
              dictionary objects for each result
            - done to avoid serializing error when serving sqlite3.row
              objects in flask
        • get_common_deaths() -> list
            - simple query to retrieve top 10 causes of death
        • get_deaths_by_age(age: str) -> list
            - calls connect_db with age value
        • get_deaths_by_race(race: str) -> list
            - calls connect_db with race value
        • get_random_entry() -> dict
            - queries random entry in cdc mortality database
            - passed random entry through human_readable_cdc_mort module
        • get_detailed_query(sex: str, age: str, race: str) -> dict
            - queries cdc mortality results by sex, age, and race
'''


def get_sql_file(cmd):
    path = os.path.join(DIR_PATH + sql_files[cmd])
    with open(path, 'r') as f:
        ret = f.read()
    return ret


def connect_db(query, value=None):
    conn = sqlite3.connect(os.path.join('databases/cdc_mortality.db'))
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    if value is not None:
        result = conn.execute(query, [value])
    else:
        result = conn.execute(query)
    ret = result.fetchall()
    conn.close()
    return ret


def build_dict(query):
    ret = []
    for item in query:
        ret.append(dict(count=item[0], cod=cod(item[1])))
    return ret


def get_common_deaths():
    sql = get_sql_file('cod_query')
    query = connect_db(sql)
    return build_dict(query)


def get_deaths_by_age(age):
    sql = get_sql_file('age_query')
    query = connect_db(sql, age.zfill(3))
    return build_dict(query)


def get_deaths_by_race(code):
    sql = get_sql_file('race_query')
    query = connect_db(sql, code)
    return build_dict(query)


def get_random_entry():
    sql = get_sql_file('random_query')
    conn = sqlite3.connect(os.path.join('databases/cdc_mortality.db'))
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    res = cur.execute(sql)
    ret = res.fetchone()
    conn.close()
    return ret


def get_detailed_query(sex, age, race):
    sql = get_sql_file('detailed')
    conn = sqlite3.connect(os.path.join('databases/cdc_mortality.db'))
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(sql, [
        age.zfill(3),
        gr(race),
        cs(sex)
    ])
    ret = result.fetchall()
    conn.close()
    return build_dict(ret)
