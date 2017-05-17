from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from base import Base

engine = create_engine('sqlite:///venues.db', echo=False)

class Venue(Base):

    __tablename__="venues"

    id = Column(Integer, primary_key=True)
    capacity = Column(Integer)
    name = Column(String)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    zipcode = Column(String)

    def __repr__(self):
        return "{}\n{}, {}, {} {}\nCAPACITY: {}".format(self.name, self.street, self.city, self.state, self.zipcode, self.capacity)
