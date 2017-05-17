import requests
import json
from sys import exit
from sqlite3 import dbapi2 as sqlite3


# def zc_db_query(zip_code):
#     """Queries by zip code"""
#     rv = sqlite3.connect("zipcode.db")
#     rv.row_factory = sqlite3.Row
#     cur = rv.execute('SELECT * FROM ZIPS WHERE ZIP_CODE == ?', [str(zip_code)])
#     query = cur.fetchone()
#     rv.close()
#     return query


def get_key(f_name: str) -> str:
    """"Retrieve API key from file"""
    with open(f_name, 'r') as f:
        key = f.read()
        key = key.replace("\n", "")
    return key


# def zip_to_coords(zip_code):
#     """Return coordinates of a zipcode"""
#     query = zc_db_query(zip_code, 'coordinates')
#     lat, lon = query[5], query[6]
#     return lat, lon
#
#
# def cs_from_zip(zip_code):
#     """Return City, State from zipcode"""
#     query = zc_db_query(zip_code)
#     city, state = query[2], query[3]
#     return city, state


def get_aq_weather(lat, lon):
    """Gets air quality and weather information from Simple Weather API"""
    headers = {
        "X-Mashape-Key": get_key("mashape.txt"),
        "Accept": "application/json",
    }
    params = {
        "lat": lat,
        "lng": lon,
    }
    aq_url = "https://simple-weather.p.mashape.com/aqi"
    wth_url = "https://simple-weather.p.mashape.com/weather"

    aq_r = requests.get(aq_url, params=params, headers=headers)
    wth_r = requests.get(wth_url, params=params, headers=headers)
    print(aq_r.text)
    return aq_r.text, wth_r.text

# def get_crime_data(zcode):
#     lat, lon = zip_to_coords(zcode)
#     headers = {
#         "X-Mashape-Key": get_key("mashape.txt"),
#         "Accept": "application/json"
#     }
#     params = {
#         'enddate': strftime("%m/%d/%Y"),
#         'lat': lat,
#         'long': lon,
#         'startdate': '12/01/2015'
#     }
#     url = 'https://jgentes-Crime-Data-v1.p.mashape.com/crime'
#
#     r = requests.get(url, params=params, headers=headers)
#     j_data = r.json()
#
#     return j_data


def get_crime_score(lat, lon):
    """Gets crime score (only usable in a few cities)"""
    headers = {
        "X-Mashape-Key": get_key("mashape.txt"),
        "Accept": "application/json",
    }
    params = {
        "f": "json",
        "id": "",
        "lat": lat,
        "lon": lon,
    }
    url = "https://crimescore.p.mashape.com/crimescore"

    resp = requests.get(url, params=params, headers=headers)
    data = json.loads(resp.text)
    grade = data["gradedetail"]
    print(resp.text)
    return grade


def get_avg_income(ip_addr: str) -> str:
    """Call average income API endpoint, return income for user's area"""
    headers = {
        "X-Mashape-Key": get_key("mashape.txt"),
        "Accept": "application/json",
    }
    params = {
        "ip_address": ip_addr,
        "fields": "income",
        "pretty": "true",
    }
    url = 'https://income.p.mashape.com/api/income/%s' % (ip_addr)

    resp = requests.get(url, params=params, headers=headers)
    data = json.loads(resp.text)
    return data["income"]


def get_ip_zcode():
    url = "http://www.freegeoip.net/json/"
    resp = requests.get(url)
    resp_json = json.loads(resp.text)
    zip_code = resp_json['zip_code']
    ip_addr = resp_json['ip']
    lat = resp_json['latitude']
    lon = resp_json['longitude']
    return ip_addr, zip_code, lat, lon


def get_cs() -> 'str, str':
    url = "http://www.freegeoip.net/json/"
    resp = requests.get(url)
    resp_json = json.loads(resp.text)
    return resp_json["city"], resp_json["region_name"]


def get_location() -> dict:
    """Build, return Location object parameters"""
    ip_addr, zcode, lat, lon = get_ip_zcode()
    city, state = get_cs()
    ret = {
        "zipcode": zcode,
        "latitude": lat,
        "longitude": lon,
        "city": city,
        "state": state
    }
    return ret


def get_results() -> dict:
    """Build, return Result object parameters"""
    ip_addr, zcode, lat, lon = get_ip_zcode()
    score = get_crime_score(lat, lon)
    aq, weather = get_aq_weather(lat, lon)
    income = get_avg_income(ip_addr)
    ret = {
        "zipcode": zcode,
        "score": score,
        "air_quality": aq,
        "weather": weather,
        "income": income,
    }
    return ret
