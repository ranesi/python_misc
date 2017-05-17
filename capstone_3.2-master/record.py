from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from base import Base

engine = create_engine('sqlite:///records.db', echo=False)

class Record(Base):

    __tablename__="records"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    country = Column(String)
    catches = Column(Integer)

    def __repr__(self):

        return "ID: {} NAME: {} COUNTRY: {} CATCHES: {}".format(self.id, self.name, self.country, self.catches)

Base.metadata.create_all(engine)
