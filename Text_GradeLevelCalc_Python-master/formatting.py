'''

This file exists ONLY to make the main file look pretty.

Love,

Rick

'''

def printLine():
    '''Prints line 40 characters in length.'''
    x=0
    while x!= 40:
        print('-',end='')
        x+=1
    print()

def printBar():
    '''Prints a single vertical line. Unnecessary? Probably!'''
    print('|',end='')

def newLine():
    '''Basically an alias for printing a newline'''
    print('')

def addSpace(x):
    '''Generates number of spaces based on int parameter. Surprisingly useful.'''
    y=0
    while y!=x: 
        print(' ',end='')
        y+=1
        
def wordBox(text):
    '''Creates a fancy text box in the console using input string.'''

    #counters for loop
    words = text.split()
    x=len(words)+2
    y=0

    #loop to generate text box
    for i in range(x+1):
        if i == 0 or i == x:
            printLine()
        elif i < x-1:
            printBar()
            spaces = 38-len(words[y])
            if spaces%2 == 0:
                addSpace(spaces//2)
                print(words[y],end='')
                addSpace(spaces//2)
            else:
                addSpace(spaces//2)
                print(words[y],end='')
                addSpace(spaces//2+1)
            printBar()
            print()
            y+=1
