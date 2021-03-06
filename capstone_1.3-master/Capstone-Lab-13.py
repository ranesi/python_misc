import json
import sys
from urllib.request import urlopen

def main():
    while True:
        title = input("\nName of movie: ")

        #change spaces to '+' to call API
        formattedTitle = title.replace(" ","+")

        url = "http://www.omdbapi.com/?t=%s&tomatoes=true&r=json" % (formattedTitle)
        '''
            This code taken from 'Introducing Python'
            page 5 (heh)
        '''
        try: #attempt to retrieve movie score from OMBD API
            #open url
            response = urlopen(url)
            #read, save response
            contents = response.read()
            #decode
            text = contents.decode("utf-8")
            #convert to json
            data = json.loads(text)
            #search response by key (tomato score)
            try:
                score = data['tomatoMeter']
                print('\nThe TomatoMeter score for %s is %s!' % (title, score))

                if int(score) >= 80:
                    print('Certified fresh!')

                elif int(score) >= 50 and int(score) <= 79:
                    print('Not too bad...')

                else:
                    print('This movie STINKS.')

            except: #NOT FOUND
                print('Couldn\'t find the movie.')

        except: #SOMETHING IS GOING ON
            print('Something wicked that way went. API FAILURE.')

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
