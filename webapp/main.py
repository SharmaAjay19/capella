from flask import Flask, request, render_template
from Logger import Logger
app = Flask(__name__, static_folder='static')
logger = Logger()

@app.route('/')
def home_page():
	return render_template('audio.html', filepath='/static/file1.m4a')

if __name__ == '__main__':
	PORT = 5001
	app.run('0.0.0.0', PORT, ssl_context='adhoc')