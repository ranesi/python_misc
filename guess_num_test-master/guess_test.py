import unittest
from unittest.mock import patch
import guess_the_number as g

class TestGame(unittest.TestCase):

    def test_in_range(self):
        self.assertEqual(True, g.in_range(5,0,10))
        self.assertEqual(True, g.in_range(25,0,1000))
        self.assertEqual(False, g.in_range(1,5,10))

    def test_check_guess(self):
        self.assertEqual(True, g.check_guess(5,5))
        self.assertEqual(False,g.check_guess(11,2))

    @patch('builtins.input', side_effect=[3,6])
    @patch('builtins.print')
    def test_get_range(self, mock_print, mock_input):
        g.get_range()
        mock_print.assert_called_with(3, 6)

    @patch('builtins.input',side_effect=['quetzacoatl'])
    def test_erroneous_number(self, mock_input):
        with self.assertRaises(ValueError):
            g.get_number()

    @patch('builtins.input',side_effect=['y','n','BBQ','Y'])
    def test_play_again(self, mock_input):
        self.assertEqual(True, g.play_again())
        self.assertEqual(False, g.play_again())
        self.assertEqual(False, g.play_again())
        self.assertEqual(True, g.play_again())


    @patch('builtins.print')
    def test_print_result(self, mock_print):
        g.print_result(5,5)
        mock_print.assert_any_call('You guessed correctly!')
        g.print_result(1,1000)
        mock_print.assert_any_call('Too Low!!!')
        g.print_result(1000,1)
        mock_print.assert_any_call('Too High!!!')


    @patch('builtins.input', side_effect=['5'])
    @patch('builtins.print')
    def test_game_win(self, mock_print, mock_input):
        g.guess_loop(0,10,5)
        mock_print.assert_any_call('You guessed correctly!')
        mock_print.assert_any_call('You won in 1 guesses!')

    @patch('builtins.input', side_effect=['8','10'])
    @patch('builtins.print')
    def test_game_loss(self, mock_print, mock_input):
        g.guess_loop(1,10,10)
        mock_print.assert_any_call('Too Low!!!')
        mock_print.assert_any_call('You guessed correctly!')
        mock_print.assert_any_call('You won in 2 guesses!')
