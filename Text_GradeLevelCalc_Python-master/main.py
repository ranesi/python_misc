__author__='rick'

'''

Main file for the program!

        BE AWARE
This program is dependent on
the following libraries
(downloaded elsewhere) -

-NumPy
 <http://www.numpy.org>
-NLTK (natural language toolkit)
 <http://www.nltk.org>
-from NLTK, cmudict
    -Do the following:
    >>import nltk
    >>nltk.download()
    #from here, select cmudict
    #under "copora"
'''

import misc

def main():
    misc.mainLoop() # look in misc for main loop
    
if __name__=='__main__':
    main()
