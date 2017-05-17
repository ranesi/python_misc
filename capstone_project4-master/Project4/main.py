from flask import Flask, request, redirect, url_for, render_template, flash, Markup
from flask_sqlalchemy import SQLAlchemy
from tables import Location, FoursquareResult, GoogleResult
from api import build_foursquare_obj
from directions import get_coords, get_city_state, get_directions

app = Flask(__name__)

config = dict(
    DEBUG=True,
    SECRET_KEY='dev',
    SQLALCHEMY_DATABASE_URI='sqlite:///tables.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
app.config.from_envvar('PROJECT4_SETTINGS', silent=True)
app.config.update(config)


db = SQLAlchemy(app)

# Global variable used to store zipcode
gl_zip = ''

MIN_ZIP_LEN = 5


def add_to_db(zip_code: str) -> None:
    """Determine if location exists within db, add results if not"""
    if Location.query.filter_by(zipcode=zip_code).first() is None:
        fs_list = build_foursquare_obj(zip_code)
        add_fs_results(fs_list)
        add_location(zip_code)
        add_directions(zip_code)
    else:
        pass


def add_fs_results(fs_list: list) -> None:
    for item in fs_list:
        db.session.add(item)
    db.session.commit()
    db.session.close()


def add_location(zip_code: str) -> None:
    lat, lon = get_coords(zip_code)
    city, state = get_city_state(zip_code)
    loc = Location(zipcode=zip_code, latitude=lat, longitude=lon, city=city, state=state)
    db.session.add(loc)
    db.session.commit()
    db.session.close()


def add_directions(zip_code: str) -> None:
    directions = get_directions(zip_code)
    gr = GoogleResult(zipcode=zip_code, directions=directions)
    db.session.add(gr)
    db.session.commit()
    db.session.close()


@app.route('/')
@app.route('/index')
def index() -> 'render_template()':
    """Query database, populate template with entries"""
    global gl_zip
    locations = Location.query.filter_by(zipcode=gl_zip)
    fs_results = FoursquareResult.query.filter_by(zipcode=gl_zip)
    g_result = GoogleResult.query.filter_by(zipcode=gl_zip).first()
    if g_result is not None:
        gr = Markup(g_result.directions)
    else:
        gr = None
    return render_template('index.html', locations=locations, fs_results=fs_results,
                           g_results=gr)


@app.route('/find', methods=['POST'])
def get_location_data() -> 'redirect()':
    """Request zipcode from form, send to DB function"""
    global gl_zip
    gl_zip = [request.form['zipcode']]
    gl_zip = gl_zip[0]
    if len(gl_zip) >= MIN_ZIP_LEN \
            and valid_int(gl_zip):  # determine if the entered value is a valid zipcode
        add_to_db(gl_zip)
        flash('Operation succeeded!')
    else:
        flash('Enter a valid zip code, please.')
    return redirect(url_for('index'))


def valid_int(zip_code: str) -> bool:
    try:
        int(zip_code)
        return True
    except ValueError:
        return False
#
# if __name__ == '__main__':
#     app.run()
