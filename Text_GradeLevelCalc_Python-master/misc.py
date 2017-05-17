from misc import *
from formatting import *

import log
import os.path
import statistics
import sys
import text

global version
global email

################INFO############################################################
version = '0.01a'
email = 'richanesi@gmail.com'
################################################################################

def badInput():
    '''Alias to make the program more readable.'''
    printLine()
    print('Invalid input!')
    printLine()

def copyinfo():
    '''Something needed to be printed in the "about" section.'''
    printLine()
    wordBox('Version:' + version)
    print('Questions? Email',email)

def funStuff(gl):
    newLine()
    if gl > 8.5 and gl < 9.5:
        print('With a grade level of',str(gl)+', this would')
        print('be acceptable for publication in a news')
        print('paper.')
    elif gl < 8.5:
        print('With a grade level of',str(gl)+', this would')
        print('be too basic for a newspaper.')
    else:
        print('With a grade level of',str(gl)+', this would')
        print('be too verbose for a newspaper.')
    newLine()
    print('2016 candidate: ',end='')
    if gl > 10:
        print('SANDERS')
    elif gl < 10 and gl > 9:
        print('FIORINA')
    elif gl < 9 and gl > 8:
        print('CRUZ')
    elif gl < 8 and gl > 7:
        print('CLINTON')
    elif gl < 7 and gl > 6:
        print('JINDAL')
    elif gl < 6 and gl > 5:
        print('CARSON')
    else:
        print('TRUMP')

def getFile():
    '''Returns file contents as a string.'''
    x = 0
    printLine()
    filename = str(input("File to be analyzed: "))#)+'.txt') coercion unnecessary
    while x == 0:
        if os.path.isfile(filename) == True: # does the file exist?
            filevar = open(filename,'r')
            text = filevar.read()
            filevar.close()
            x = 1
        else:
            print('Invalid input!')
            filename = str(input("File to be analyzed: "))
    
    printLine()
    return text,filename

def greet():
    printLine()
    print('Please select an option: ')
    print('\t(a) analyze a file')
    print('\t(s) settings')
    print('\t(b) about')
    print('\t(q) quit')
    option = input(':')
    return option

def optionSelect():
    printLine()
    print('Which index should be used?')
    print('(1)\t\tFlesch-Kincaid')
    print('(2)\t\tAutomated')
    print('(3)\t\tSMOG')
    print('(4)\t\tAverage')
    var=input(':')
    return var

def printAll(se,w,sy,re,gl,ari,op,smog,avg,filename):
    ''' Keeping print functions outta main, damnit. '''
    wordBox(filename)
    print('TOTAL SENTENCES: \t',se)
    print('TOTAL WORDS: \t\t',w)
    print('TOTAL SYLLABLES: \t',sy)
    
    if op == '1':
        print('Flesch RI:\t\t',re)
        print('F-K Grade Level:\t',gl)
        funStuff(gl)
    elif op == '2':
        print('ARI Score:\t\t',ari)
        print('ARI Level:\t\t',text.ariLevel(ari))
        funStuff(text.ariLevel(ari))
    elif op == '3':
        print('SMOG GL:\t\t',smog)
        funStuff(smog)
    elif op == '4':
        print('Avg. GL:\t\t',avg)
        print('Variance:\t\t',round(statistics.variance([gl,ari,smog]),2))
        funStuff(avg)

    newLine()
    log.logger(se,w,sy,re,gl,ari,smog,avg,filename)
    

################################################################################

    
def mainLoop():
    '''Main loop of the program. Could've been in the "main" file, but nooooo.'''
    
    quitProg = False #used by main loop, true == quit program
    wordBox('Readability & Grade-Level Calculator')
    newLine()
    setting='3'

    while quitProg == False: #main loop
        option = greet()
        if option == 'a':
            textName,filename = getFile()
            tClass = text.readability(textName)
            tClass.process()
            a,b,c,d,e,f,g,h = tClass.get()
            printAll(a,b,c,d,e,f,setting,g,h,filename)
        elif option == 'b':
            copyinfo()
        elif option == 's':
            setting=optionSelect()
        elif option == 'q':
            quitProg = True
        else:
            badInput()

    sys.exit(0)
