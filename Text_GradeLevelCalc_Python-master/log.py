import os.path

def logger(se,w,sy,re,gl,ari,smog,avg,filename):
    '''Function writes analysis to log file'''
    x=0
    fname='report'+str(x)+'.txt'

    while os.path.isfile(fname) == True: #checks to see if log file exists
        x+=1
        fname='report'+str(x)+'.txt'
    
    print('Log written to',fname)
    file = open(fname,'w')
    file.write(logString(se,w,sy,re,gl,ari,smog,avg,filename))
    file.close()
    

def logString(se,w,sy,re,gl,ari,smog,avg,filename):
    '''Creates, returns pretty table.'''

    list1=['SE','W','SY','RL','FK GL','ARI','SMOG','AVG']
    list2=[se,w,sy,re,gl,ari,smog,avg]

##    var={'1. Sentences':se,
##         '2. Words':w,
##         '3. Syllables':sy,
##         '4. RL':re,
##         '5. FK GL':gl,
##         '6. ARI':ari,
##         '7. SMOG':smog,
##         '8. AVG':avg}

    varStr=filename
    x=0

    for item in list1: #loop builds output string

        varStr = varStr + '\n' + item + '\t' + ':' + '\t' + str(list2[x])
        x+=1

    return varStr
