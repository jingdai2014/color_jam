import sqlite3
from flask import Flask, request, redirect, render_template, g
from contextlib import closing

# configuration
DATABASE = '/tmp/color.db'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
	db = getattr(g, 'db', None)
	if db is not None:
		db.close()

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/add', methods=['POST'])
def pick_color():
	g.db.execute('insert into entries (uid, time, color) values (?, ?, ?)',
		[request.form['uid'], request.form['time'], request.form['color']])
	g.db.commit()
	flash('Your choice was successfully saved. Thanks!')
	return redirect(url_for('home'))

if __name__ == '__main__':
	app.run()

