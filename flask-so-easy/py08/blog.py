#-*-coding:utf-8-*-
from flask import Flask, request, render_template, redirect, make_response

app = Flask(__name__)
user_list = ['alen', 'max', 'aw']

@app.route('/login/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		# cookies获取
		username = request.form.get('username')
		if username in user_list:
			# cookies设置
			response = make_response(redirect('/index/'))
			response.set_cookie('username', value=username, max_age=300)
			return response
		else:
			return redirect('login')
	else:
		return render_template('login.html')

@app.route('/index/')
def index():
	username = request.cookies.get('username')
	if username:
		return render_template('index.html', username=username)
	else:
		return redirect('login')

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
