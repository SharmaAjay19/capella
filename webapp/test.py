from flask import Flask, request, render_template
from Logger import Logger
app = Flask(__name__, static_folder='static')
logger = Logger()

@app.route('/')
def home_page():
	return render_template('applyFilters.html')

if __name__ == '__main__':
   PORT = 5001
   app.run('0.0.0.0', PORT, ssl_context='adhoc')
   #app.run('0.0.0.0', PORT, ssl_context='adhoc')