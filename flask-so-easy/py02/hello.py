from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
	username = 'alen'
	return render_template('index.html', username=username)

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 80)
