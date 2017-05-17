from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from record import Record

def init_session():
    engine = create_engine('sqlite:///records.db', echo=False)
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    return Session()
# Session = sessionmaker(bind=engine)
# s = Session()
def add_entry(entry):
    s = init_session()
    r = Record(name=entry[0],country=entry[1],catches=entry[2])
    s.add(r)
    s.commit()
    s.close()

def del_entry(n):
    s = init_session()
    for record in s.query(Record).filter_by(id=n):
        s.delete(record)
    s.commit()
    s.close()

def show_entries():
    s = init_session()
    print('---------------------------------------------------------------')
    for record in s.query(Record):
        print(record)
    print('---------------------------------------------------------------')
