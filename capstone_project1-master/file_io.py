
fname = 'scores.txt'

def error():
    print('%s not found!' % (fname))

def read_highscore():
    try:
        with open(fname, 'r') as scores:
            for line in scores:
                print(line)
            scores.close()
    except Exception:
        error()

def write_highscore(name):
    temp = ''
    try:
        with open(fname, 'r') as scores:
            for line in scores:
                temp += line
            scores.close()
        with open(fname, 'w') as scores:
            temp += "%s" % (name)
            scores.write(temp)
            scores.close()
    except Exception:
        error()
