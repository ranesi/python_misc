import sys
import sqlite3
from functools import wraps


def init_db():
    return 'create table if not exists records (id integer primary key autoincrement, name text, country text, catches integer)'

def db_arg(sql, args):
    db = sqlite3.connect('database.db')
    cur = db.cursor()
    cur.execute(sql, args)
    db.commit()
    db.close()

def db(sql):
    db = sqlite3.connect('database.db')
    cur = db.cursor()
    cur.execute(sql)
    db.commit()
    db.close()

def add_record():
    return 'insert into records (name, country, catches) values (?,?,?)'


def show_records():
    db = sqlite3.connect('database.db')
    cur = db.cursor()
    cur.execute('select * from records')
    for row in cur:
        print(row)
    db.close()


def delete_record():
    return 'delete from records where id = (?)'


def process_cmd(cmd):
    if cmd == 'a':
        db_arg(add_record(), get_info())
    elif cmd == 's':
        show_records()
    elif cmd == 'd':
        db_arg(delete_record(),get_id())
    elif cmd == 'q':
        sys.exit()
    else:
        print('Invalid selection!')

def get_id():
    id = int(input("ID of record to delete: "))
    return [id]

def get_info():
    name = input("What is the name of the record holder? ")
    country = input("Country of origin? ")
    catches = input("How many catches? ")
    return name, country, catches


def get_options():
    cmd = input(show_options())
    return cmd.lower()


def show_options():
    print('(A)dd record, (S)how records, (D)elete record, (Q)uit')


def main():
    while True:
        cmd = get_options()
        process_cmd(cmd)

if __name__=='__main__':
    db(init_db())
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
