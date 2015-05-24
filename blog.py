from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/regist/', methods = ['GET', 'POST'])
def regist():
	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')
		return '%s, %s' % (username, password)
	else:
		return render_template('regist.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)


