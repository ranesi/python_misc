import os


def message(s, test = False):
    '''Prints message after clearing screen'''
    #stackoverflow.com/questions/2084508
    if test == False:
        os.system('cls' if os.name == 'nt' else 'clear')
    print(s)


def to_continue(s):
    '''Prints string, awaits blank input from user (press enter to continue)'''
    while True:
        c = input(s)
        if c == '':
            break


def show_commands():
    '''Display main menu commands'''
    commands = '''1) Add entry to specified database
2) Show entries from specified database
3) Delete entry by ID
4) Advanced queries
5) Quit'''
    message(commands)


def select_adv_query():
    '''Display/retrieve advanced query menu/selection'''
    valid_queries = ['1', '2', '3']
    queries = '''1) Show total # of entries per database
2) Search employees by venue
3) Search artists by event
    '''
    while True:
        message(queries)
        adv_query = input('')
        if adv_query in valid_queries:
            return adv_query


def select_table():
    '''Display table menu/retrieve selection'''
    valid_tables = ['1', '2', '3', '4']
    tables = '''1) Venues
2) Employees
3) Events
4) Artists'''
    while True:
        message(tables)
        table = input('')
        if table.lower() in valid_tables:
            return table.lower()
        else:
            message('Command not recognized!')


def get_cmd():
    '''Display command menu/retrieve selection'''
    valid_cmd = ['1','2','3','4','5']
    while True:
        cmd = input('')
        if cmd.lower() in valid_cmd:
            return cmd.lower()
        else:
            print('Command not recognized!')


def get_venue_info():
    '''Requests venue information from user, returns as dictionary'''
    while True:
        try:
            cap = int(input('Enter capacity: '))
            name = input('Enter name of venue: ')
            st = input('Enter street address: ')
            city = input('Enter city: ')
            state = input('Enter state: ')
            zcode = input('Enter zipcode: ')
            rent = float(input('Monthly rent: '))
            return {'capacity':cap, 'name':name, 'street':st, 'city':city, \
                'state':state, 'zcode':zcode, 'rent':rent}
        except ValueError:
            message('Incorrect input type for capacity (must be INT).')


def get_employee_info():
    '''Requests, returns employee info'''
    x = 0
    while x < 4:
        try:
            vid = int(input('Enter VN# of employee\'s venue: '))
            title = input('Employee job title: ')
            fname = input('First name: ')
            lname = input('Last name: ')
            phone = input('Phone #: ')
            wage = float(input('Hourly wage: '))
            status = input('Employment status (FT/PT):' )
            return {'venue_id':vid, 'title':title, 'fname':fname, 'lname':lname, \
                'phone':phone, 'wage':wage, 'status':status}
        except ValueError:
            print('Incorrect input type for venue ID (must be INT).')


def get_event_info():
    '''Requests, returns event info'''
    x = 0
    while x < 4:
        try:
            vid = int(input('Enter venue ID: '))
            ts = int(input('Number of tickets sold: '))
            tp = float(input('Price per ticket: '))
            return {'venue_id':vid, 'tickets_sold':ts, 'ticket_price':tp}
        except ValueError:
            print('Incorrect entry type.')


def get_artist_info():
    '''Requests, returns artist info'''
    x = 0
    while x < 4:
        try:
            eid = int(input('Enter event ID number (if any): '))
            name = input('Name of artist: ')
            fee = float(input('Fee charged by artist: '))
            genre = input('Genre of artist: ')
            phone = input('Phone number: ')
            email = input('Email: ')
            return {'event_id': eid, 'name':name, 'fee':fee, 'genre':genre, \
                'phone':phone, 'email':email}
        except ValueError:
            print('Incorrect entry type.')


def get_id():
    '''Requests, returns integer from user'''
    while True:
        try:
            num = int(input('Please enter ID number of entry: '))
            return num
        except ValueError:
            print('Incorrect input type!')


def print_line(word=''):
    '''Prints a line 40 characters in length'''
    print('{:*^40}'.format(word))
