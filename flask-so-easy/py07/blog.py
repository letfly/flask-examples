from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/regist/', methods=['GET', 'POST'])
def regist():
	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')
		conn = sqlite3.connect('my.db')
		cursor = conn.cursor()
		sql = 'insert into user (username, password) values(?, ?)'
		cursor.execute(sql, (username, password))
		conn.commit()
		cursor.close()
		conn.close()
		return '%s regist ok!' % (username)
	else:
		return render_template('regist.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
