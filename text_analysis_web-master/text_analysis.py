import os
import textrazor
from text import Text
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

def get_key():
    with open('key.txt', 'r') as f:
        temp = f.read()
        temp = temp[:len(temp) - 1]
    return temp

textrazor.api_key = get_key()

'''
    For the most part, this app is based on the "flaskr" Flask tutorial
        -Namely the DB and flask app items
    https://github.com/pallets/flask/tree/master/examples/flaskr
'''

fields = 'title, topic0, topic1, topic2, sentences, words, syllables, characters, polysyllables, re, gl, ari, smog'


app=Flask(__name__)


app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'text_analysis.db'),
    DEBUG=False,
    SECRET_KEY='dev'
))
app.config.from_envvar('TEXT_ANALYSIS_SETTINGS', silent=True)


def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    '''
    Read schema file, create database.
    WARNING: this will remove all entries!
    '''
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    init_db()
    print('DB INIT SUCCESS')


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
@app.route('/index')
def index():
    db = get_db()
    cursor = db.execute('select %s from entries order by id desc' % (fields))
    entries = cursor.fetchall()
    return render_template('index.html', entries=entries)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/add', methods=['POST'])
def add_text():
    '''Insert form data into db'''
    title, text = [request.form['title'],request.form['text']]
    db = get_db()
    t = calculate_input(title, text)
    topic = get_topics(text)

    db.execute('insert into entries (topic0, topic1, topic2, title, sentences, words, syllables, characters, polysyllables, re, gl, ari, smog) values (?,?,?,?,?,?,?,?,?,?,?,?,?)',
                [topic[0], topic[1], topic[2], t.title,
                t.sentences, t.words, t.syllables, t.characters,
                t.poly_syllables, t.re, t.gl, t.ari, t.smog])
    db.commit()
    flash("Analysis successful!")

    return redirect(url_for('index'))


def get_topics(text):
    '''Call textrazor API, generate a list of topics'''
    ret = []
    tro = textrazor.TextRazor(extractors=['topics'])
    try:
        resp = tro.analyze(text)
        x = 0
        for topic in resp.topics():
            if topic.score > 0.5:
                ret.append(topic.label)
    except:
        pass
    while len(ret) <= 3:
        ret.append('')
    return ret



def calculate_input(title, text):
    analyzed_text = Text(title, text)
    analyzed_text.process()
    return analyzed_text

def get_key():
    with open('key.txt', 'r') as f:
        temp = f.read()
        temp = temp[:len(temp-1)]
#if __name__=='__main__':
#    app.run(debug=False)
