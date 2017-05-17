import random, sys

correct = 'You guessed correctly!'
too_low = 'Too Low!!!'
too_high = 'Too High!!!'

def get_number(s = 'test'):
    # while True:
    try:
        ret = int(input('Enter the %s value' % (s)))
        return ret
    except ValueError:
        raise ValueError
        print('Incorrect value type!')

def get_range():
    '''Set the high and low values for the random number'''
    minimum = get_number('minimum')
    maximum = get_number('maximum')
    print(minimum, maximum)
    return minimum, maximum

def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def in_range(guess, low, high):
    if low <= guess <= high:
        return True
    return False


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return True
    if guess > secret or guess < secret:
        return False


def play_again():
    cmd = input('Would you like to play again? y/n ')
    cmd = cmd.lower()
    if cmd == 'y':
        return True
    else:
        return False

def print_result(guess, secret):
    if guess == secret:
        print(correct)
    elif guess < secret:
        print(too_low)
    else:
        print(too_high)


def guess_loop(low, high, secret):
    #initialize game values
    guess_counter = 0
    win = False

    while not win:
        #guess until correct
        guess = get_number('guess')
        win = check_guess(guess, secret)
        guess_counter += 1
        print_result(guess, secret)
        if win:
            print('You won in {} guesses!'.format(guess_counter))
            

def main():
    (low, high) = get_range()
    secret = generate_secret(low, high)
    while True:
        guess_loop(low, high, secret)
        if play_again():
            continue
        else:
            break
    print('Be seeing you!')
    sys.exit()

if __name__ == '__main__':
        main()
