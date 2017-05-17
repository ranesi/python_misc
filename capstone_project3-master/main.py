import sys, orm, ui
from tables import Venue, Employee, Event, Artist


def add_rows(t):
    '''Used to obtain and pass object to orm header'''
    if t == '1':
        entry = ui.get_venue_info()
        v = Venue(**entry)
        orm.add_entry(v)

    elif t == '2':
        entry = ui.get_employee_info()
        em = Employee(**entry)
        orm.add_entry(em)

    elif t == '3':
        entry = ui.get_event_info()
        ev = Event(**entry)
        orm.add_entry(ev)

    elif t == '4':
        entry = ui.get_artist_info()
        a = Artist(**entry)
        orm.add_entry(a)


def show_rows(t):
    '''Calls specified SELECT * statement'''
    if t == '1':
        orm.show_venues()

    elif t == '2':
        orm.show_employees()

    elif t == '3':
        orm.show_events()

    elif t == '4':
        orm.show_artists()


def delete_rows(t):
    '''Gets ID number, passes ID number and table to DB interface'''
    num = ui.get_id()
    orm.del_entry(num, t)


def adv_query(c):
    '''Select, call appropriate advanced query'''
    if c == '1':
        orm.get_db_info()
    elif c == '2':
        orm.show_employees_venues(ui.get_id())
    elif c == '3':
        orm.show_artists_events(ui.get_id())

def process_cmd(cmd):
    '''Executes the correct command'''
    if cmd == '1':
        add_rows(ui.select_table())

    elif cmd == '2':
        show_rows(ui.select_table())

    elif cmd == '3':
        delete_rows(ui.select_table())

    elif cmd == '4':
        adv_query(ui.select_adv_query())

    elif cmd == '5':
        sys.exit(0)


def main():
    while True:
        ui.show_commands()
        cmd = ui.get_cmd()
        process_cmd(cmd)


if __name__=='__main__':
    main()
