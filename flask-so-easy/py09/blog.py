#-*-coding:utf-8-*-
from flask import Flask, request, render_template, redirect, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
user_list = ['alen', 'max', 'aw']

@app.route('/login/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		# cookies获取
		username = request.form.get('username')
		if username in user_list:
			# cookies设置
			session['username'] = username
			return redirect('index')
		else:
			return redirect('login')
	else:
		return render_template('login.html')

@app.route('/index/')
def index():
	username = session.get('username')
	if username:
		return render_template('index.html', username=username)
	else:
		return redirect('login')

@app.route('/logout/')
def logout():
	pass

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
