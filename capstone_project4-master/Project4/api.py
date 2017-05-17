import foursquare
from time import sleep
from tables import FoursquareResult


# Get a list of keys & identifiers from text file
def get_keys() -> list:
    temp = ''
    with open('keys.txt', 'r') as f:
        for line in f:
            temp += line
    keys = temp.split('\n')
    return keys


# Parse keys from their identifiers
def parse_foursquare_keys(keys: list) -> list:
    client_id = keys[0].split('=')
    client_secret = keys[1].split('=')
    keys_dict = {client_id[1], client_secret[1]}
    keys_list = list(keys_dict)
    return keys_list


# Set up foursquare client for get_results
def get_foursquare_client() -> object:
    keys = parse_foursquare_keys(get_keys())
    client_id = keys[0]
    client_secret = keys[1]
    client = foursquare.Foursquare(client_id=client_id, client_secret=client_secret)
    return client


# Get the first 3 results from "Top Picks" in a certain area
def get_results(location: str) -> object:
    client = get_foursquare_client()
    while True:
        try:
            results = client.venues.explore(params={'near': location, 'section': 'topPicks', 'limit': '3'})
            return results
        except foursquare.InvalidAuth: # foursquare has problems with userless authorization
            sleep(0.5)
            print("Retrying...")


# Returns venue names. Location can be a zip code or a city/town name
# Example return: ['Electric Fetus', 'Surly Brewing Company', "Sebastian Joe's Ice Cream Cafe"]
def get_foursquare_names(location):
    venues = get_results(location)
    names_list = []
    for x in range(3):
        names_list.append(venues['groups'][0]['items'][x]['venue']['name'])
    return names_list


# Addresses are returned as a list of 3 lists, each containing 2 address lines
# Example return: [['2000 4th Ave S (at Franklin Ave)', 'Minneapolis, MN 55404'],
#                  ['520 Malcolm Ave SE (SE 5th St)', 'Minneapolis, MN 55414'],
#                  ['4321 Upton Ave S', 'Minneapolis, MN 55410']]
def get_foursquare_addresses(location):
    venues = get_results(location)
    address1 = []
    address2 = []
    address3 = []
    address1.append(venues['groups'][0]['items'][0]['venue']['location']['formattedAddress'][0])
    address1.append(venues['groups'][0]['items'][0]['venue']['location']['formattedAddress'][1])
    address2.append(venues['groups'][0]['items'][1]['venue']['location']['formattedAddress'][0])
    address2.append(venues['groups'][0]['items'][1]['venue']['location']['formattedAddress'][1])
    address3.append(venues['groups'][0]['items'][2]['venue']['location']['formattedAddress'][0])
    address3.append(venues['groups'][0]['items'][2]['venue']['location']['formattedAddress'][1])
    addresses = []
    addresses.append(address1)
    addresses.append(address2)
    addresses.append(address3)
    return addresses


# Returns prices of each venue, ranging from 1-4 dollar signs
# Note: Not all venues have an associated price. These venues will return "None provided"
# Example return: ['$', '$$$', 'None provided']
def get_foursquare_prices(location):
    venues = get_results(location)
    price_list = []
    for x in range(3):
        if 'price' in venues['groups'][0]['items'][x]['venue']:
            price_list.append(venues['groups'][0]['items'][x]['venue']['price']['currency'])
        else:
            price_list.append("None provided")
    return price_list


# Returns rating of each venue, in a scale from 1-10
# Note: Not all venues have an associated rating. These venues will return "None provided"
# Example return: ['9.8', 'None provided', '9.2']
def get_foursquare_rating(location):
    venues = get_results(location)
    rating_list = []
    for x in range(3):
        if 'rating' in venues['groups'][0]['items'][x]['venue']:
            rating_list.append(str(venues['groups'][0]['items'][x]['venue']['rating']))
        else:
            rating_list.append("None provided")
    return rating_list


# Returns each venue's website url
# Note: Not all venues have an associated website. These venues will return "None provided"
# Example return: ['http://www.first-avenue.com', 'http://izzysicecream.com', 'http://www.minneapolisparks.org']
def get_foursquare_website_url(location):
    venues = get_results(location)
    web_url_list = []
    for x in range(3):
        if 'url' in venues['groups'][0]['items'][x]['venue']:
            web_url_list.append(venues['groups'][0]['items'][x]['venue']['url'])
        else:
            web_url_list.append("None provided")
    return web_url_list


# Returns the photo url provided by Foursquare for each venue
# Note: Not all venues have an associated image url. These venues will return "None provided"
# Example return: ['None provided', 'https://igx.4sqi.net/img/general/original/697943_8_Y-mixR.jpg', 'None provided']
def get_foursquare_image_url(location):
    venues = get_results(location)
    pic_url_list = []
    for x in range(3):
        if 'photourl' in venues['groups'][0]['items'][x]['tips'][0]:
            pic_url_list.append(venues['groups'][0]['items'][x]['tips'][0]['photourl'])
        else:
            pic_url_list.append("None provided")
    return pic_url_list


# Returns a short description of each venue
# Note: Not all venues have an associated description. These venues will return "None provided"
def get_foursquare_description(location):
    venues = get_results(location)
    pic_url_list = []
    for x in range(3):
        if 'text' in venues['groups'][0]['items'][x]['tips'][0]:
            pic_url_list.append(venues['groups'][0]['items'][x]['tips'][0]['text'])
        else:
            pic_url_list.append("None provided")
    return pic_url_list


def build_foursquare_obj(zip_code='55116') -> '[FoursquareResult]':
    """Create the FoursquareResult objects needed"""
    ret = []

    names = get_foursquare_names(zip_code)
    addresses = get_foursquare_addresses(zip_code)
    prices = get_foursquare_prices(zip_code)
    ratings = get_foursquare_rating(zip_code)
    urls = get_foursquare_website_url(zip_code)
    images = get_foursquare_image_url(zip_code)
    descriptions = get_foursquare_description(zip_code)

    for x in range(3):
        ret.append(FoursquareResult(
            zipcode=zip_code,
            name=names[x],
            address1=addresses[x][0],
            address2=addresses[x][1],
            price=prices[x],
            rating=ratings[x],
            url=urls[x],
            pic_url=images[x],
            description=descriptions[x],
        ))

    return ret

