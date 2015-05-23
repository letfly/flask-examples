from flask import Flask

# determine the working directory
app = Flask(__name__)

# access routes
@app.route('/') 
def hello_world():
	return '<h1>hello world flask</h1>'

if __name__ == '__main__':
	# run a development server
	app.run(host='0.0.0.0', port=80)
