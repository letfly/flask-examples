#-*-coding:utf-8-*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
	# base type
	username = 'alen'
	# list
	nav_list = [u'首页', u'经济', u'文化', u'科技', u'娱乐']
	# dict
	blog = {'title':'blog 1', 'content':'my blog, my blog'}
	return render_template('index.html', username=username, nav_list=nav_list, blog = blog)

if __name__ == '__main__':
	app.run()
