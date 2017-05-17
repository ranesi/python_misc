from sqlalchemy import Column, Integer, Float, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#conn = create_engine('sqlite:///:memory:', echo=True) #testing purposes
conn = create_engine('sqlite:///mgmt.db', echo=False)
Base = declarative_base()


class Venue(Base):

    __tablename__='venues'

    id = Column(Integer, primary_key=True)
    # gig_id = Column(Integer, ForeignKey('gigs.id'))
    employees = relationship("Employee")
    capacity = Column(Integer)
    name = Column(String)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    zcode = Column(String)
    rent = Column(Float)
    #other fields

    def __repr__(self):
        ret = 'VN#{:>5} Cap:{:>6}\n{}\n{}\n{}, {} {}\nRENT{:>15.2f}'.format(self.id,\
        self.capacity, self.name, self.street, self.city, self.state,\
        self.zcode, self.rent)
        return ret


class Employee(Base):

    __tablename__='employees'

    id = Column(Integer, primary_key=True)
    venue_id=Column(Integer, ForeignKey('venues.id'))
    title = Column(String)
    fname = Column(String)
    lname = Column(String)
    phone = Column(String)
    wage = Column(Float)
    status = Column(String)

    def __repr__(self):
        ret = 'EID{} VN#{}\n{}, {}\n{}\n{}\n{}\n${:>.2f}'.format(self.id, self.venue_id,\
            self.lname, self.fname, self.title, self.phone, self.status, self.wage)
        return ret


class Event(Base):

    __tablename__='events'
    id = Column(Integer, primary_key=True)
    artists = relationship('Artist')
    venue_id=Column(Integer, ForeignKey('venues.id'))
    tickets_sold = Column(Integer)
    ticket_price = Column(Float)

    def __repr__(self):
        ret = 'EvID#{:>6}\nVN#{:>8}\nTckt sold:{} Tckt cost: {:>.2f}'.format(self.id,\
            self.venue_id, self.tickets_sold, self.ticket_price)
        return ret


class Artist(Base):

    __tablename__='artists'

    id = Column(Integer, primary_key = True)
    event_id=Column(Integer, ForeignKey('events.id'))
    name = Column(String)
    fee = Column(Float)
    genre = Column(String)
    phone = Column(String)
    email = Column(String)

    def __repr__(self):
        ret = 'ArID#{:>6}Ev#{:>8}{}, {}\n{}\n{} | {}'.format(self.id,\
            self.event_id, self.name, self.genre, self.phone, self.email)
        return ret


Base.metadata.create_all(conn)
