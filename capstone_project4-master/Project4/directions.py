from sqlite3 import dbapi2 as sqlite3
from googlemaps import convert
import urllib.error
import urllib.request
import urllib.parse
import re
import ssl
import requests
import json


def get_key(f_name):
    with open(f_name, 'r') as f:
        temp = f.read()
    return temp


def zipcode_query(zip_code, type='ll'):
    """SQLite3 query for zipcode database."""
    rv = sqlite3.connect("zipcode.db")
    rv.row_factory = sqlite3.Row
    cur = rv.execute('SELECT * FROM ZIPS WHERE ZIP_CODE == ?', [str(zip_code)])
    query = cur.fetchone()
    rv.close()
    if type == 'll':
        return query[5], query[6]
    else:
        return query[2], query[3]


def get_coords(zip_code):
    """Returns the latitude, longitude of a given zip code"""
    lat, lon = zipcode_query(zip_code, 'll')
    return lat, lon


def get_city_state(zip_code):
    """Gets the city, state of a given zipcode
        **NOT the city-state e.g. Venice"""
    city, state = zipcode_query(zip_code)
    return city, state


def get_client_location(): #Getting user location
    try:
        url = "http://www.freegeoip.net/json/"
        # locationInfo = json.loads(urllib.request.urlopen(urlForLocaction).read())
        location_json = json.loads(requests.get(url).text)
        # print (locationInfo)
        lat = str(location_json['latitude'])
        lon = str(location_json['longitude'])
        return lat, lon #(Return user latitude and longitude)

    except urllib.error.URLError as e: #(URl error exception)
        print(e.reason)


def get_directions(zip_code):

    html_tags = r'<[^>]+>' # Html tags to get rid of while printing the direction

    client_location = get_client_location()

    # get string of latitude, longitude
    location = get_coords(zip_code)

    maps = get_key("googlemaps.txt") # Google maps API Key

    # Convert latitude and longitude but useless tho
    address = convert.latlng(client_location)
    destination = convert.latlng(location)

    # Getting the full Url with the map, origin point, destination, driving mode, and api key
    direction = str("origin=" + address + "&destination=" + destination + "&mode=driving" + "&key=" + maps)
    urlDirection = str("https://maps.googleapis.com/maps/api/directions/json?" + direction)

    # print (urlDirection)
    # Got it from the link below supposed to get rid of ssl error
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1) #(http://stackoverflow.com/questions/27835619/ssl-certificate-verify-failed-error)

    request = urllib.request.Request(urlDirection)
    UrlResp = urllib.request.urlopen(request, context=gcontext)

    UrlPlease = UrlResp.read().decode(encoding="utf-8")
    Nextresult = json.loads(UrlPlease)

    ret = ""
    #Printing the direction with no html tags (https://docs.python.org/3/library/re.html)
    for Nmap in range(0, len(Nextresult['routes'][0]['legs'][0]['steps'])):
        MapDir = Nextresult['routes'][0]['legs'][0]['steps'][Nmap]['html_instructions']
        # will preserve HTML tags
        # FinalDir = re.sub(html_tags, ' ', MapDir)
        ret += "<li>" + MapDir + "</li>" + "\n"

    return ret
