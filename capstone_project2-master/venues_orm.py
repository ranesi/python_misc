from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def init_session():
    engine = create_engine('sqlite:///venues.db', echo=False)
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    return Session()

def add_entry():
    pass

def del_entry():
    pass

def show_entries():
    pass
