import simplejson
import os
import psycopg2
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, json, flash

app = Flask(__name__)


@app.route('/')
def show_entries():
    conn = psycopg2.connect(database="cphqieql", user="cphqieql", host="75.126.166.187",password="mW3yvNGp3wHFGuFp56mn4gdkdKb1UJ5T")
    cur = conn.cursor()
    cur.execute('SELECT title, text FROM entries ORDER BY id DESC')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)


@app.route('/song', methods=['GET'])
def get_produto():
    conn = psycopg2.connect(database="cphqieql", user="cphqieql", host="jumbo.db.elephantsql.com",password="mW3yvNGp3wHFGuFp56mn4gdkdKb1UJ5T")
    cur = conn.cursor()
    cur.execute('SELECT name, artist, album from Song')
    entries = cur.fetchall()
    songs_as_dict = []
    for song in entries:
        song_as_dict = {
            'name' : song[0],
            'artist' : song[1],
            'album' : song[2]}
        songs_as_dict.append(song_as_dict)
    return simplejson.dumps(songs_as_dict)



@app.route('/add', methods=['POST'])
def add_entry():
    conn = psycopg2.connect(database="cphqieql", user="cphqieql", host="jumbo.db.elephantsql.com",password="mW3yvNGp3wHFGuFp56mn4gdkdKb1UJ5T")
    cur = conn.cursor()
    cur.execute("INSERT INTO entries (title, text) VALUES (%s, %s)", (request.form['title'], request.form['text']) )
    conn.commit()
    cur.close()
    conn.close()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))




@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run(host='0.0.0.0', port=int(port))


