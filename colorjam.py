import sqlite3
from flask import Flask, request, redirect, render_template, g, jsonify, flash, url_for
from contextlib import closing
import datetime
from application import db
from application.models import Colors
from brightness_analysis import process_color
import collections

app = Flask(__name__)
app.secret_key = "compassion"
app.config.from_object(__name__)

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


@app.route('/colors', methods=['GET'])
def get_tasks():

    c = Colors.query.all()
    colors = []

    for color_row in c:

    	color = {"id":color_row.id, "uid":color_row.uid, "time":color_row.time, "color":color_row.color, "valence":color_row.valence}
        colors.append(color)
    return jsonify({'colors': colors})


@app.route('/analysis', methods=['GET'])
def get_analysis():
    print "haha"
    # c = Colors.query.all()
    # colors = []

    # for color_row in c:

    #     color = {"id":color_row.id, "uid":color_row.uid, "time":color_row.time, "color":color_row.color, "valence":color_row.valence}
    #     colors.append(color)

    # print colors

    # colorDict = {'colors': colors}
    # print colorDict

    # colorNames = process_color(colorDict)

    return "hahaha"


if __name__ == '__main__':
	app.run()
	# connect_db()
	# init_db()

