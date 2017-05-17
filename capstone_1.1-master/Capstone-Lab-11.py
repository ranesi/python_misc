import random

def main():
    number = random.randint(1,10)
    guess = int(input('GUESS A NUMBER FROM 1-10! '))
    if guess == number:
        print('You got it! Here is an ampersand for you... &')
    else:
        print('NO! I was thinking of %i' % number)

if __name__=='__main__':
    main()
