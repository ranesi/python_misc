'''

This file is where text analysis lives.

Includes readability class, which stores:
    -string of text
    -# of sentences
    -# of words
    -# syllables
    -grade level
    -readability index, on a scale from 0 - 100

Functions:
    -FK,ARI,SMOG readability
    -

'''

import math
import statistics
from nltk.corpus import cmudict

#global variables###############################################################

dictionary=cmudict.dict()

stops = '.?!'
vowels = 'aeiouy'
digraphs = ['aa','ae','ai','au','ay',
            'ea','ee','ei','eo','eu','ey',
            'ie',
            'oa','oe','oi','oo','ou','oy',
            'ue','uy',
            'ya','ye','yi','yo','yu']
edigraphs = ['ae','ie','oe','ue']
trigraphs = ['iou','eou']

################################################################################
    
class readability:

    def __init__(self,text):

        self._tStr = text
        self._sentences = 0
        self._words = 0
        self._syllables = 0
        self._characters = 0
        self._poly = 0
        self._GL = 0
        self._RE = 0
        self._ARI = 0
        self._smog = 0
        self._mean = 0

    def process(self):

        self._sentences,self._words,self._syllables,self._characters,self._poly = countStr(self._tStr)
        self._RE=readEase(self._words,self._sentences,self._syllables)
        self._GL=gradeLevel(self._words,self._sentences,self._syllables)
        self._ARI = autoRead(self._sentences,self._words,self._characters)
        self._smog=smogLevel(self._sentences,self._poly)
        self._mean=round(statistics.mean([self._GL,self._ARI,self._smog]),2)

    def get(self):

        return self._sentences,self._words,self._syllables,self._RE,self._GL,self._ARI,self._smog,self._mean

#helpy functiony################################################################

def sylNum(word): #special thanks to R. Penman for his condensed return statement
    '''Break words into phonemes using cmudict, create counting # of vowels'''
    return [len(list(y for y in x if y[-1].isdigit())) for x in dictionary[word.lower()]]

def countStr(text):
    '''Returns number of sentences, words, syllables, characters, polysyllables as tuple.'''

    charCount=len(text)
    stopCount=0
    syllCount=0
    wordCount=len(text.split())
    polyCount=0
    
    x=0
    
    text = text.lower()
    sList = text.split()
    temp=''
    lTemp=[]
    
    
    for word in sList:
        #vars for subloop (unknown word handling)
        skip=0
        y=0
        pTemp=0
        if word[0].isalpha() == False: #presumably not a word
            wordCount=wordCount-1
        if word[-1] in stops: #assuming that stops are sentences
            stopCount+=1
        if word[-1].isalpha() == False: #remove punctuation
            temp = word[0:(len(word)-1)]
        else:
            temp = word
        if temp in dictionary:
            lTemp=sylNum(temp)
            syllCount+=int(lTemp[0])
            if int(lTemp[0])>=3: #is word polysyllable
                polyCount+=1
        else: # for words not in dictionary, count vowels
            for a in temp:
                if skip==0:
                    if a in vowels:
                        if len(temp[y:])>3 and a+temp[y+1]+temp[y+2] in trigraphs:
                            pTemp+=1
                            syllCount+=1
                            skip=2
                        elif len(temp[y:])>2 and a+temp[y+1] in digraphs:
                            pTemp+=1
                            syllCount+=1
                            skip+=1
                        
                        elif len(temp[y:])>3 and a+text[y+2] in edigraphs:
                            pTemp+=1
                            syllCount+=1
                            skip=2
                        else:
                            pTemp+=1
                            syllCount+=1
                else:
                    skip=skip-1
                if pTemp >= 3:
                    polyCount+=1
                y+=1
        
    return (stopCount,wordCount,syllCount,charCount,polyCount)

def smogLevel(se,p):
    '''Returns SMOG grade level of a text '''

    smog=math.sqrt((p*(30/se))*(1.0430**2))+3.1291
    return round(smog,2)

def readEase(w,se,sy):
    '''Returns reading ease as calculated by the Flesch readability equation'''
    
    var=(206.835-(1.015*(w/se))-(84.6*(sy/w)))
    return round(var,2)

def gradeLevel(w,se,sy):
    '''Returns grade level as calculated by the Flesch-Kincaid grade level equation'''
    
    var=((0.39*(w/se))+(11.8*(sy/w))-15.59)
    return round(var,2)

def autoRead(se,w,c):

    var=(4.71*(c/w))+(0.5*(w/se))-21.43
    var=int(round(var,0))
    if var > 14:
        var = 14
    if var < 1:
        var = 1
    return var

def ariLevel(ari):

    if ari <= 1:
        return 1
    else:
        return ari-1
