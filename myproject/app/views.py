from app import app
'''
@app.route('/')
def index():
    return 'hello world, hello flask'
'''
from flask import render_template, flash, redirect, session, url_for, request, g
from app import db
from models import User, Post, ROLE_USER, ROLE_ADMIN

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/adduser/<nickname>/<email>')
def adduser(nickname, email):
    u = User(nickname=nickname, email=email)
    try:
	db.session.add(u)
	db.session.commit()
	return 'add successful'
    except Exception, e:
	return 'something go wrong'
@app.route('/getuser/<nickname>')
def getuser(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    return render_template('user.html', user=user)
@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

