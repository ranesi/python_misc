from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///records.db', echo=False)   # Create engine. echo=True turns on logging
Base = declarative_base()
