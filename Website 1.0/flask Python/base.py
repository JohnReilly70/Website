from flask import Flask

base = Flask(__name__)

@app.route('/index')
def index():
	return render_template('index.html')


@app.route('/content')
def content():
	return render_template('index.html')


@app.route('/about')
def about():
	return render_template('index.html')


@app.route('/python')
def python():
	return render_template('index.html')

if __name__="__main__"

base.run(debug=True)