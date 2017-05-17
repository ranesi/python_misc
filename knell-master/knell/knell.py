from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from .tables import Location, Result
from .api import get_results, get_location


app = Flask(__name__)

conf = dict(
    DEBUG=False,
    SECRET_KEY='dev',
    SQLALCHEMY_DATABASE_URI='sqlite:///tables.db'
)

app.config.update(conf)
app.config.from_envvar('KNELL_SETTINGS', silent=True)

db = SQLAlchemy(app)

gbl_zip = ''


def db_add() -> None:
    """Retrieve API results, store in DB"""
    global gbl_zip

    result = get_results()
    location = get_location()
    gbl_zip = location["zipcode"]

    db.session.add(Location(**location))
    db.session.add(Result(**result))

    db.session.commit()
    db.session.close()


@app.route('/')
@app.route('/index')
def index() -> render_template:
    global gbl_zip
    if gbl_zip == '':
        locations, results = None, None
    else:
        locations = Location.query.filter_by(zipcode=gbl_zip).order_by(Location.id.desc()).first()
        results = Result.query.filter_by(zipcode=gbl_zip).order_by(Result.id.desc()).first()
    return render_template('index.html', locations=locations, results=results)


@app.route('/find', methods=['POST'])
def find_info() -> redirect:
    """This is what happens when users click buttons."""
    db_add()
    return redirect(url_for('index'))

