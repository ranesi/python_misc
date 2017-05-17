import requests
import random
from time import time
import os


'''Fetch a random image from the V&A collections'''

vam_images = 'vam_images'

def fetch_random_image_set(query):
    ''' Query V&M API, returns dictionary with random set of images matching query
    Query pararameters are encoded by requests, so can be included in URL.
    Returns data as dictonary. '''

    params = { 'q' : query, 'image': 1, 'random':1 }
    url = 'http://www.vam.ac.uk/api/json/museumobject/search'

    response = requests.get(url, params=params)

    return response.json()


def fetch_image(image_data):
    '''Download image and save to disk. Return filename.'''

    print(image_data)
    print(int(time()))
    print(time())


    image_id = image_data['fields']['primary_image_id']
    url = 'http://media.vam.ac.uk/media/thira/collection_images/{}/{}.jpg'.format(image_id[:6], image_id)

    print(url)

    image_response = requests.get(url, stream=True)

    filename = 'vam_{}_{}.jpg'.format(image_id, int(time()))

    filepath = os.path.join(vam_images, filename)

    with open(filepath, 'wb') as file:
        for chunk in image_response.iter_content(chunk_size=128):
            file.write(chunk)

    return filepath

    #TODO error handling


def download_random_vam_image(query='landscape'):

    try :
        os.mkdir(vam_images)
    except FileExistsError:
        pass

    random_image_response = fetch_random_image_set(query)
    random_images = random_image_response['records']
    image_data = random.choice(random_images)
    filepath = fetch_image(image_data)
    return filepath


def main():
    download_random_vam_image()


if __name__ == '__main__':
    main()
