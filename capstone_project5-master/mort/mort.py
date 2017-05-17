from flask import Flask, request, redirect, url_for, render_template, flash, \
    Markup, session
import human_readable_cdc_mort as hr
import graphing as gr
import query_cdc
import json
import sqlite3
import os

app = Flask(__name__)

config = dict(
    DEBUG=True,
    SECRET_KEY='dev key!',
)

app.config.from_envvar('MORT_SETTINGS', silent=True)
app.config.update(config)


@app.route('/', methods=['GET', 'POST'])
def display_results(*args, **kwargs):
    if request.method == 'POST':
        try:
            cond = request.form['condition']
            if cond != 'random':
                if cond == 'by_age':
                    age = request.form['age']
                    session['args'] = get_info(cond, age)
                elif cond == 'by_race':
                    race = request.form['race']
                    session['args'] = get_info(cond, race)
                elif cond == 'top_10':
                    session['args'] = get_info(cond)
                try_delete_session_var('kwargs')
            else:
                kwargs = get_info(cond)
                session['kwargs'] = kwargs
                try_delete_session_var('args')
        except KeyError:
            flash('You must select something!')
            try_delete_session_var('args')
            try_delete_session_var('kwargs')

        # return redirect(url_for('index'))
        return redirect(url_for('display_results'))

    entries = check_session_vars('args')
    entry = check_session_vars('kwargs')
    graph = make_graph(entries)

    return render_template('display_results.html', entry=entry,
                           entries=entries, graph=graph)


@app.route('/detailed_search', methods=['POST'])
def detailed_search():

    sex = request.form['sex'].title()
    age = request.form['age']
    race = request.form['race'].title()
    session['args'] = get_info('detailed', [sex, age, race])
    print(session['args'])
    return redirect(url_for('display_results'))


def get_info(cond, value=None):
    if cond == 'top_10':
        ret = query_cdc.get_common_deaths()
    elif cond == 'by_age':
        ret = query_cdc.get_deaths_by_age(value)
    elif cond == 'by_race':
        ret = query_cdc.get_deaths_by_race(hr.get_race_by_name(value))
    elif cond == 'random':
        ret = query_cdc.get_random_entry()
        ret = hr.readable_death(ret)
    elif cond == 'detailed':
        ret = query_cdc.get_detailed_query(value[0], value[1], value[2])
    return ret


def make_graph(r):
    if r is not None:
        return gr.graph_result(r)
    else:
        return None


def try_delete_session_var(var):
    try:
        del session[var]
    except KeyError:
        pass


def check_session_vars(var):
    try:
        session[var]
        return session[var]
    except KeyError:
        entries = None
