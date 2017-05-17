import ui, time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import Venue, Employee, Event, Artist
# from sqlalchemy.ext.declarative import declarative_base

CONTINUE = 'Press ENTER to load more results...'
END = 'No more results! Press ENTER to return to main menu...'


def init_session():
    '''Connect to database, initialize and return session'''
    db = 'sqlite:///mgmt.db'
    engine = create_engine(db, echo=False)
    session = sessionmaker(bind = engine)
    return session()


def finalize(s):
    '''Commit changes and close connection to database'''
    s.commit()
    s.close()


def add_entry(entry):
    '''Add passed ORM entity to database'''
    s = init_session()
    s.add(entry)
    finalize(s)


def del_entry(i, t):
    '''Search for row by ID, delete entry'''
    s = init_session()
    if t == '1':
        for x in s.query(Venue).filter_by(id = i):
            s.delete(x)
    elif t == '2':
        for x in s.query(Employee).filter_by(id = i):
            s.delete(x)
    elif t == '3':
        for x in s.query(Event).filter_by(id = i):
            s.delete(x)
    elif t == '4':
        for x in s.query(Artist).filter_by(id = i):
            s.delete(x)
    finalize(s)


def show_venues():
    '''SELECT * query for venues table'''
    s = init_session()
    ui.print_line()
    x = 0
    total = 0
    try:
        for venue in s.query(Venue):
            print(venue)
            total += venue.rent
            ui.print_line()
            time.sleep(0.1)
            if x >= 3:
                ui.to_continue(CONTINUE)
                x = 0
                ui.message('')
                continue
            x += 1
    except:
        pass
    ui.print_line()
    print('TTL MONTHLY RENT\n-\t\t${:>10.2f}'.format(total))
    print('ANNUAL\n-\t\t${:>10.2f}'.format(total * 12))
    ui.to_continue(END)


def show_employees():
    '''SELECT * query for employees table'''
    s = init_session()
    ui.print_line()
    x = 0
    try:
        for em in s.query(Employee):
            print(em)
            if em.status.lower() == 'ft':
                sal = em.wage * 40
            elif em.status.lower () == 'pt':
                sal = em.wage * 20
            print('Weekly est. pay ${:.2f}, monthly ${:.2f}'.format(sal, (sal * 4)))
            ui.print_line()
            time.sleep(0.1)
            if x >= 3:
                ui.to_continue(CONTINUE)
                x = 0
                ui.message('')
                continue
            x += 1
    except:
        pass
    ui.to_continue(END)


def show_events():
    '''SELECT * query for events table'''
    s = init_session()
    ui.print_line()
    x = 0
    try:
        for ev in s.query(Event):
            print(ev)
            print('Total sales: {:>17.2f}'.format(ev.tickets_sold * ev.ticket_price))
            ui.print_line()
            time.sleep(0.1)
            if x >= 3:
                ui.to_continue(CONTINUE)
                x = 0
                ui.message('')
                continue
            x += 1
    except:
        pass
    ui.to_continue(END)


def show_artists():
    '''SELECT * entry for artists table'''
    s = init_session()
    ui.print_line()
    x = 0
    try:
        for a in s.query(Artist):
            print(a)
            ui.print_line()
            time.sleep(0.1)
            if x >= 3:
                ui.to_continue(CONTINUE)
                x = 0
                ui.message('')
                continue
            x += 1
    except:
        pass
    ui.to_continue(END)


def get_db_info():
    '''Get count of entries from all tables, print to console output'''
    s = init_session()
    ui.print_line()
    venues = s.query(Venue).count()
    employees = s.query(Employee).count()
    events = s.query(Event).count()
    artists = s.query(Artist).count()
    print('Venues\t\t{:>10}\nEmployees\t{:>10}\nEvents\t\t{:>10}\nArtists\t\t{:>10}'.format(venues, employees, events, artists))
    ui.to_continue(END)


def show_employees_venues(id_num):
    '''Query employees by venue'''
    s = init_session()
    ui.print_line()
    total = 0.0
    for entry in s.query(Employee).filter_by(venue_id = id_num):
        print(entry)
        ui.print_line()
        if entry.status == 'FT':
            total += entry.wage * 40
        else:
            total += entry.wage * 20
    print('Annual amount spent on employee wages: {:>.2f}'.format(total * 52))
    ui.to_continue(END)


def show_artists_events(id_num):
    '''Query artists by event'''
    s = init_session()
    ui.print_line()
    total = 0.0
    for entry in s.query(Artist).filter_by(event_id = id_num):
        print(entry)
        total += entry.fee
        ui.print_line()
    print('Total amount spent on artist fees at event {}: {:>.2f}'.format(id_num, total))
    ui.to_continue(END)
