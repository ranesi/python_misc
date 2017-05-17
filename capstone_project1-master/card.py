import random

suits = ['Hearts','Diamonds','Spades','Clubs']
ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

'''
    The code contained herein is based on Card.py by Allen B. Downey
    URL:
        <http://www.greenteapress.com/thinkpython/code/Card.py>
'''

class Card:
    '''
    Object representing a card. Fields:
    suit: 0 - 3     (Heart-Clubs)
    rank: 0 - 12    (Ace-King)
    '''
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        temp = "%s of %s" % (ranks[self.rank], suits[self.suit])
        return temp

    def __eq__(self, other):
        return (self.suit, self.rank) == (other.suit, other.rank)

    def __lt__(self,other):
        return self.rank < other.rank

    def get(self):
        return self.rank

class Deck:
    '''
    Represents a deck of cards. Fields:
    cards = list of card objects (52)

    Methods:
    rank_list - returns list containing only ranks (for go fish)
    sort_/shuffle_cards - either sorts cards (ASC) or randomizes them
    add_/remove_card - adds/remove a card from cards: list
    remove_all - removes ALL elements with (x) rank
    move_card - pops (x) number of cards to other deck
    '''
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(13):
                card = Card(suit,rank)
                self.cards.append(card)

    def __str__(self):
        temp = ''
        for card in self.cards:
            temp += str(card) + '\n'
        return temp

    def __eq__(self, other):
        for card in self.cards:
            if card not in other.cards:
                return False
        return True

    def rank_list(self):
        res = []
        for card in self.cards:
            res.append(card.rank)
        return res

    def sort_cards(self):
        self.cards.sort()

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def remove_all(self, x):
        '''
            "Inspired by" Stack Overflow answer (kind of):
            <http://stackoverflow.com/questions/2793324/is-there-a-simple-way-
            to-delete-a-list-element-by-value-in-python>
        '''
        self.cards = [y for y in self.cards if y.rank != x]

    def move_card(self, other, number):
        x = 0
        while x < number:
            try:
                other.cards.append(self.cards.pop())
            except IndexError:
                pass
            x += 1

class Hand(Deck):
    '''Hand subclass = deck w/out filling procedure on init (basically)'''
    def __init__(self):
        self.cards = []
