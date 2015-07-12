#!flask/bin/python
#from flask import Flask
#
#app = Flask(__name__)
#@app.route('/')
#@app.route('/index')
#def index():
#    return "Hello, World!"
#app.run(debug=True)

from app import app
app.run(debug=True, port=8000)
