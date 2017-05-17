from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tables.db'
db = SQLAlchemy(app)


class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    zipcode = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    city = db.Column(db.String)
    state = db.Column(db.String)

    def __repr__(self):
        pass


class FoursquareResult(db.Model):
    __tablename__ = 'foursquare_results'

    id = db.Column(db.Integer, primary_key=True)
    zipcode = db.Column(db.String)
    name = db.Column(db.String)
    address1 = db.Column(db.String)
    address2 = db.Column(db.String)
    price = db.Column(db.String)
    rating = db.Column(db.String)
    url = db.Column(db.String)
    pic_url = db.Column(db.String)
    description = db.Column(db.String)

    def __repr__(self):
        ret = ''
        return ret


class GoogleResult(db.Model):
    """Object for HTML directions received from the Google Maps API"""
    __tablename__ = 'google_results'

    id = db.Column(db.Integer, primary_key=True)
    zipcode = db.Column(db.String)
    directions = db.Column(db.String)

    def __repr__(self):
        ret = ''
        return ret
