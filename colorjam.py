import sqlite3
from flask import Flask, request, redirect, render_template, g, jsonify, flash, url_for
from contextlib import closing
import datetime
from application import db
from application.models import Colors

# configuration
# DATABASE = '/tmp/color.db'
# DEBUG = True

app = Flask(__name__)
app.secret_key = "compassion"
app.config.from_object(__name__)

# def connect_db():
# 	return sqlite3.connect(app.config['DATABASE'])

# def init_db():
# 	with closing(connect_db()) as db:
# 		with app.open_resource('schema.sql', mode='r') as f:
# 			db.cursor().executescript(f.read())
# 		db.commit()

# @app.before_request
# def before_request():
# 	g.db = connect_db()

# @app.teardown_request
# def teardown_request(exception):
# 	db = getattr(g, 'db', None)
# 	if db is not None:
# 		db.close()

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/add', methods=['POST'])
def pick_color():

    color_entered = Colors(int(request.form['uid']), str(datetime.datetime.now()), request.form['color'], int(request.form['valence']))
    
    db.session.add(color_entered)
    db.session.commit()        
    db.session.close()

    return redirect(url_for('home'))

	# g.db.execute('insert into entries (uid, time, color, valence) values (?, ?, ?, ?)',
	# 	[request.form['uid'], str(datetime.datetime.now()), request.form['color'], request.form['valence']])
	# g.db.commit()
	# flash('Your choice was successfully saved. Thanks!')


@app.route('/colors', methods=['GET'])
def get_tasks():

    c = Colors.query.all()
    colors = []

    for color_row in c:

    	color = {"id":color_row.id, "uid":color_row.uid, "time":color_row.time, "color":color_row.color, "valence":color_row.valence}
        colors.append(color)

    # cur = g.db.execute('select * from entries')
    # entries = [{"id":row[0], "uid":row[1], "time":row[2], "color":row[3], "valence":row[4]} for row in cur.fetchall()]
	# return db
    return jsonify({'colors': colors})

if __name__ == '__main__':
	app.run()
	# connect_db()
	# init_db()

