from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/post')
def post():
	return render_template('post.html')

@app.route('/about')
def about():
	return render_template('about.html')	

bootstrap=Bootstrap(app)