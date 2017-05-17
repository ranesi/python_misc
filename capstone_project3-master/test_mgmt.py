import unittest, orm, ui
from unittest.mock import patch
import main as mgmt
from tables import Venue, Employee, Event, Artist

ui.test = True

class TestMGMT(unittest.TestCase):

############################################
#       MAIN
############################################

    def test_add_rows(self):
        pass

    def test_show_rows(self):
        pass

    def test_delete_rows(self):
        pass

    def test_process_cmd(self):
        pass

############################################
#       UI
############################################

    @patch('builtins.print')
    def test_message(self, mock_print):
        ui.message('addis ababa', True)
        mock_print.assert_any_call('addis ababa')

    @patch('builtins.print')
    def test_show_commands(self, mock_print):
        ui.show_commands()
        mock_print.assert_any_call('''1) Add entry to specified database
    2) Show entries from specified database
    3) Delete entry by ID
    4) Advanced queries
    5) Quit''')

    def test_select_adv_query(self):
        pass

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['A','marky mark and the funky bunch', '3'])
    def test_select_table(self, mock_input, mock_print):
        ui.select_table()
        mock_print.assert_any_call('Command not recognized!')
        ui.select_table()
        mock_print.assert_any_call('Command not recognized!')
        self.assertEqual('3', ui.select_table())

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['WRONG','a','1'])
    def test_get_cmd(self, mock_input, mock_print):
        ui.get_cmd()
        mock_print.assert_any_call('Command not recognized!')
        ui.get_cmd()
        mock_print.assert_any_call('Command not recognized!')
        self.assertEqual('1', ui.get_cmd())

    def test_get_venue_info(self):
        pass

    def get_employee_info(self):
        pass

    def test_get_event_info(self):
        pass

    def test_get_artist_info(self):
        pass

    def test_get_id(self):
        pass

    @patch('builtins.print')
    def test_print_line(self, mock_print):
        ui.print_line()
        mock_print.assert_any_call('****************************************')
        ui.print_line('&')
        mock_print.assert_any_call('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')

############################################
#       TABLES
############################################

############################################
#       ORM
############################################

    def test_init_session(self):
        pass

    def test_finalize(self):
        pass

    def test_add_entry(self):
        pass

    def test_del_entry(self):
        pass

    @patch('builtins.print')
    def test_show_venues(self, mock_print):
        pass

    @patch('builtins.print')
    def test_show_employees(self, mock_print):
        pass

    @patch('builtins.print')
    def test_show_events(self, mock_print):
        pass

    @patch('builtins.print')
    def test_show_artists(self, mock_print):
        pass

    @patch('builtins.print')
    def test_get_db_info(self, mock_print):
        pass

    @patch('builtins.print')
    def test_show_employees_venues(self, mock_print):
        pass

    @patch('builtins.print')
    def test_show_artists_events(self, mock_print):
        pass
