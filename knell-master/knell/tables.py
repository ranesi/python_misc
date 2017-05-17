# from sqlalchemy import Column, Integer, String, Float, create_engine
# from sqlalchemy.ext.declarative import declarative_base
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tables.db'
db = SQLAlchemy(app)
# conn = create_engine('sqlite:///tables.db', echo=False)
#
# Base = declarative_base()


class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    zipcode = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    city = db.Column(db.String)
    state = db.Column(db.String)

    def __repr__(self):
        ret = "{}\n{}, {}\nLAT:\tLAT{:>10.4f}\nLON{:>10.4f}".format(self.zipcode,
                                                                    self.city,
                                                                    self.state,
                                                                    self.latitude,
                                                                    self.longitude)
        return ret


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    zipcode = db.Column(db.String)
    score = db.Column(db.String)
    air_quality = db.Column(db.Integer)
    weather = db.Column(db.String)
    income = db.Column(db.Integer)

    def __repr__(self):
        ret = "GRADE: \"{}\"\nAir Quality: {}\nWEATHER: {}\nINCOME: ${}".format(self.score, self.air_quality, self.weather,
                                                                         self.income)
        return ret

# Base.metadata.create_all(conn)
