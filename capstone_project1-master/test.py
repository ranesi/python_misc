import unittest
from unittest.mock import patch
import main as game
from card import Card, Hand, Deck

class TestGame(unittest.TestCase):

    @patch('builtins.print')
    def test_printline(self, mock_print):
        '''Test line printing function'''
        game.print_line('*',1)
        mock_print.assert_any_call('*')
        game.print_line('&',5)
        mock_print.assert_any_call('&&&&&')

    def test_isvalid(self):
        '''Test whether valid guesses return true, invalid false'''
        valid_guess = [
        'Ace','2','3','4','Queen','King'
        ]
        invalid_guess = [
        'bacon','','queene','11', u'§'
        ]
        for guess in valid_guess:
            self.assertEqual(True, game.is_valid(guess))
        for guess in invalid_guess:
            self.assertEqual(False, game.is_valid(guess))

    @patch('builtins.print')
    def test_check_match(self, mock_print):
        '''Test to check whether a match is correctly reported'''
        valid_hand = Hand()
        invalid_hand = Hand()
        for x in range(4):
            valid_hand.add_card(Card(0,4))
            invalid_hand.add_card(Card(0,x))

        self.assertEqual(1, game.check_match(valid_hand, ''))
        self.assertEqual(0, game.check_match(invalid_hand, ''))
        self.assertEqual(0, len(valid_hand.cards))
        self.assertEqual(4, len(invalid_hand.cards))

    @patch('builtins.print')
    def test_go_fish(self, mock_print):
        matched_hand1 = Hand()
        matched_hand2 = Hand()
        unmatched_hand1 = Hand()
        unmatched_hand2 = Hand()

        for x in range(5):
            matched_hand1.add_card(Card(0,x))
            matched_hand2.add_card(Card(0,x))
        unmatched_hand1.add_card(Card(1,3))
        unmatched_hand2.add_card(Card(2,11))

        self.assertEqual(True, game.go_fish('', 1, matched_hand1, matched_hand2))
        self.assertEqual(True, game.go_fish('', 4, matched_hand2, matched_hand1))
        self.assertEqual(False, game.go_fish('', 5, unmatched_hand1, unmatched_hand2))

    def test_test_victory(self):
        win_hand, lose_hand = Hand(), Hand()
        lose_hand.add_card(Card(0,0)) # losing hand > 0

        self.assertEqual(True, game.test_victory(win_hand))
        self.assertEqual(False, game.test_victory(lose_hand))

    @patch('builtins.print')
    def test_not_correct(self, mock_print):
        test_deck = Hand()
        test_hand = Hand()
        x = 1
        test_deck.add_card(Card(x,0))
        test_hand.add_card(Card(0,x))

        game.not_correct('', test_hand, test_deck, False)
        mock_print.assert_any_call(' received a Ace of Diamonds\n')

    @patch('builtins.input', side_effect=['test','bacon','abcd','quetzacoatl'])
    def test_guess_card(self, mock_input):
        usr_input = ['Test','Bacon','Abcd','Quetzacoatl']
        for x in range(4):
            self.assertEqual(usr_input[x], game.guess_card())

    def test_comp_guess(self):
        hand1 = Hand()
        hand2 = Hand()
        hand1.add_card(Card(0,0))
        hand2.add_card(Card(2,11))
        self.assertEqual(0,game.comp_guessing(hand1))
        self.assertEqual(11,game.comp_guessing(hand2))

    def test_is_command(self):

        self.assertEqual(True, game.is_command('t','true'))
        self.assertEqual(False, game.is_command('w', 'quit'))


    @patch('builtins.print')
    @patch('main.guess_card', return_value='Ace')
    @patch('main.comp_guessing', return_value=10)
    def test_game(self, mock_comp_guess, mock_guess, mock_print):
        '''Player wins game, should return true'''
        deck = Hand()
        player = Hand()
        comp = Hand()

        for x in range(3):
            player.add_card(Card(x,0))
            comp.add_card(Card(x,0))

        self.assertEqual(True, game.game(deck, player, comp))

    @patch('builtins.print')
    @patch('main.guess_card', return_value='2')
    @patch('main.comp_guessing', return_value=0)
    def test_game(self, mock_comp_guess, mock_guess, mock_print):
        '''Player loses game, should return false'''
        deck = Hand()
        player = Hand()
        comp = Hand()

        for x in range(3):
            player.add_card(Card(x,0))
            comp.add_card(Card(x,0))

        self.assertEqual(False, game.game(deck, player, comp))

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1','D','Q'])
    @patch('main.shutdown', return_value=None)
    def test_main(self, mock_shutdown, mock_input, mock_print):
        self.assertEqual(None, game.main())

    def test_card_get(self):
        c = Card(0,2)
        self.assertEqual(2, c.get())

    @patch('builtins.print')
    def test_card_string(self, mock_print):
        c = Card(0,2)
        print(str(c))
        mock_print.assert_any_call('3 of Hearts')

    def test_move_card(self):
        deck = Deck()
        hand1 = Hand()
        hand2 = Hand()
        hand1.add_card(Card(0,2))
        hand1.move_card(hand2, 1)
        self.assertEqual(2, hand2.cards[0].get())
        self.assertEqual(52, len(deck.cards))
        deck.move_card(hand1, 20)
        self.assertEqual(20, len(hand1.cards))

    def test_remove_all(self):
        hand = Hand()
        for x in range(4):
            hand.add_card(Card(x,0))
        self.assertEqual(4, len(hand.cards))
        hand.remove_all(0)
        self.assertEqual(0, len(hand.cards))

    def test_init_decks(self):
        deck, hand1, hand2 = game.init_decks()
        self.assertEqual(5, len(hand1.cards))
        self.assertEqual(5, len(hand2.cards))
        self.assertEqual(42, len(deck.cards))
