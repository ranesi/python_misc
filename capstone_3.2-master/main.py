import sys, record_orm

def add_record(entry):
    record_orm.add_entry(entry)

def show_records():
    record_orm.show_entries()

def delete_record(id):
    record_orm.del_entry(id)

def get_id(op):
    while True:
        try:
            id = int(input('Enter ID of record to %s: ' % (op)))
            return id
        except ValueError:
            print("Invalid entry!")

def get_info():
    while True:
        try:
            name = input("Name of record-holder: ")
            country = input("Country of origin: ")
            catches = int(input("Number of catches: "))
            return (name, country, catches)
        except ValueError:
            print("Invalid entry!")

def process_cmd(c):
    if c == 'a':
        add_record(get_info())
    elif c == 's':
        show_records()
    elif c == 'd':
        delete_record(get_id('delete'))
    elif c == 'q':
        sys.exit()

def get_cmd():
    cmd = input('(A)dd record, (S)how records, (D)elete records, (Q)uit: ')
    return cmd.lower()

def print_greetin():
    msg = '''
CHAINSAW JUGGLING WORLD RECORD DATABASE MAINTENANCE APPLICATION
---------------------------------------------------------------
    '''
    print(msg)

def main():
    while True:
        process_cmd(get_cmd())

if __name__=='__main__':
    print_greetin() #folksy name
    main()
