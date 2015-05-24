from flask import Flask, render_template, request
import os

app = Flask(__name__)
headimg_path = os.path.join(os.getcwd(), 'static')

@app.route('/regist/', methods=['GET', 'POST'])
def regist():
	if request.method == 'POST':
		username = request.form['username']
		headimage = request.files['headimage']
		headimage.save(os.path.join(headimg_path, headimage.filename))
		return 'user is %s, headimage is %s'%(username, headimage.filename)
	else:
		return render_template('regist.html')

if __name__ == '__main__':
	app.debug = True
	app.run()
