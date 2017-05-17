
def main():
    valid = False
    strBuild = ''

    stringIn = input("Enter a string to convert to camel case: ")

    if stringIn[0].isalpha() or stringIn[0] == '_':
        valid = True
    if stringIn[-1].isalpha() == False:
        stringIn = stringIn[:-1]

    stringIn = stringIn.split()

    for word in stringIn:
        if word == stringIn[0]:
            word = word.lower()
        else:
            word = word.title()
        strBuild += word


    print('Camel case string! \n%s' % strBuild)
    if not valid:
        print('Not a valid variable name!')
    else:
        print('It is a valid variable name!')

if __name__=='__main__':
    main()
