__author__='ranesi'

import sys
import time
from functools import wraps
from card import *
from file_io import *

welcome = '''
                GO FISH!
The game of guessing cards over and over.

    v0.0002a by Rich Anesi, Jan 16 2017
'''

def print_line(char='-', num=40):
    '''Prints line of "char" parameter characters, default len=40'''
    print(char * num) #could use .format, but this achieves the same effect

def print_hand(hand):
    '''Displays hand with (interval) pause between cards'''
    interval=0.1
    print('\nThis is your hand:')
    time.sleep(interval)
    for card in hand.cards:
        print(str(card))
        time.sleep(interval)

def add_space(x):
    '''Prints x number of spaces'''
    y = 0
    while y != x:
        print(' ', end='')
        y += 1

def word_box(text):
    '''Displays a box, prints parameter text (centered) one word per line'''
    words = text.split()
    x = len(words) + 2
    print_line()
    for word in words:
        print('|{:^38}|'.format(word))
    print_line()
    print()

def sleeper(duration):
    '''
        Adds delay to a function.
        Based on <https://docs.python.org/2/library/functools.html#functools.wraps>
        and <http://stackoverflow.com/questions/15624801/passing-a-parameter-to-the-decorator-in-python>
    '''
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            #time.sleep(duration) #disable for testing
            return function(*args, **kwargs)
        return wrapper
    return decorator

def shutdown():
    '''Gracious shutdown procedure'''
    print_line()
    print('Thanks for playing!\nsource at <https://github.com/ranesi/>')
    sys.exit()

def is_valid(guess):
    '''Determine if guess is valid input'''
    if guess in ranks:
        return True
    else:
        return False

@sleeper(0.5)
def check_match(hand, name):
    '''Checks for four-of-a-kind matches, returns score (increment)'''
    temp = hand.rank_list()
    got_point = False
    num_ranks, match, score = 13, 4, 0
    for value in range(num_ranks):
        if temp.count(value) == match:
            hand.remove_all(value)
            print_line('*')
            print('Four of a kind! %s scores!' % (name))
            print_line('*')
            got_point = True
            score+=1
            break
    if not got_point:
        print('No four-of-a-kind matches for %s...' % (name))
    return score

@sleeper(0.2)
def go_fish(name, guess, hand, other):
    '''Determines whether a guess is correct, adds/deletes guess if so'''
    print('%s guesses %s' % (name, ranks[guess]))

    for card in other.cards:
        if card.get() == guess:
            print('%s guessed correctly and receives %s!\n'
                    % (name, str(card)))
            hand.add_card(card)
            other.remove_card(card)
            return True

    return False

@sleeper(0.5)
def not_correct(name, hand, deck, is_computer=False):
    '''Function for "Go Fish" event: move card to hand (if len(deck) > 0)'''

    word_box('GO FISH!')
    if len(deck.cards) > 0:
        deck.move_card(hand, 1) #send one card to hand
        if not is_computer:
            print('%s received a %s\n' % (name, str(hand.cards[-1])))
    else:
        print('No more cards in deck!\n')

def test_victory(hand):
    '''Returns bool if victory (all cards cleared) detected'''
    if len(hand.cards) == 0:
        return True
    else:
        return False

def sort_hands(hand, other):
    '''Sort decks in ascending order'''
    hand.sort_cards()
    other.sort_cards()

@sleeper(0.2)
def guess_card():
    guess = input('\nDoes the computer have a(n) (rank): ')
    guess = guess.title()
    return guess

def comp_guessing(comp):
    guess = comp.cards[random.randint(0,len(comp.cards)-1)].get()
    return guess

def is_command(guess, string):
    if guess == string \
    or guess == string[:1]:
        print()
        return True
    return False


def victory(s, score):
    print('{} score is {}.'.format(s,score))


def init_decks():

    initial_draw = 5
    deck = Deck()
    deck.shuffle_cards()
    player = Hand()
    comp = Hand()
    deck.move_card(player, initial_draw)
    deck.move_card(comp, initial_draw)

    return deck, player, comp

def game(deck, player, comp):
    '''Game loop - Go Fish game'''
    score, comp_score = 0, 0

    print_line('-')

    while True:
        correct, comp_correct = False, False

        sort_hands(player, comp)
        print_hand(player)

        guess = guess_card()
        #check to see if user wishes to quit/resign
        if is_command(guess, 'Resign'):
            return False
        elif is_command(guess, 'Quit'):
            shutdown()

        elif is_valid(guess):
            #assign index of guess to variable (rank)
            guess_int = ranks.index(guess)
            #determine whether guess is correct
            correct = go_fish('Player', guess_int, player, comp)

            if not correct:
                not_correct('You', player, deck)
            #Computer guess = int representing random card rank
            comp_guess = comp_guessing(comp)
            #comp_correct = False
            comp_correct = go_fish('Computer', comp_guess, comp, player)

            if not comp_correct:
                not_correct('Computer', comp, deck, True)

        else:
            print('Not a valid guess...')
            time.sleep(0.2)

        #Check for matches in player/computer hands
        score += check_match(player, 'Player')
        comp_score += check_match(comp, 'Computer')

        if test_victory(player) or test_victory(comp):
            #No cards left in deck = victory
            if test_victory(player):
                victory('VICTORY! Your', score)
                return True
            else:
                victory('DEFEAT! Computer\'s', comp_score)
                return False


        #display player/computer scores
        print('Player:\t\t%s\nComputer:\t%s' % (score, comp_score))

def main():
    '''Main loop - present user with options, etc.'''
    while True:
        #Indefinitely display options screen
        option = str(input('(N)ew game, (D)isplay high scores, (Q)uit: '))

        if option.isalpha():
            option = option.title()
            if is_command(option, 'New'):
                deck, player, comp = init_decks()
                if game(deck, player, comp):
                    name = input('Name for score: ')
                    write_highscore(name)
            elif is_command(option, 'Display'):
                read_highscore()
            elif is_command(option, 'Quit'):
                #exit loop to make function testable
                break
            else:
                print('%s is not a valid entry!' % (option))
    shutdown()

if __name__=='__main__':
    print(welcome)
    main()
