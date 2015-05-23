#-*-coding:utf-8-*-
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
	# base type
	img = url_for('static', filename=u'images/选区001.png')
	return render_template('index.html', img=img)

if __name__ == '__main__':
	app.debug = True
	app.run()
