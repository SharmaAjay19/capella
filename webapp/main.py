from flask import Flask, request, render_template
from flask_uwsgi_websocket import GeventWebSocket
from Logger import Logger
app = Flask(__name__, static_folder='static')
logger = Logger()

@app.route('/')
def home_page():
	return render_template('audio.html', filepath='/static/file1.m4a')

ws = GeventWebSocket(app)
@ws.route('/websocket')
def audio(ws):
   first_message = True
   total_msg = ""
   sample_rate = 0

   while True:
      msg = ws.receive()

      if first_message and msg is not None: # the first message should be the sample rate
         sample_rate = getSampleRate(msg)
         first_message = False
         continue
      elif msg is not None:
         audio_as_int_array = numpy.frombuffer(msg, 'i2')
         doSomething(audio_as_int_array)
      else:
         break

if __name__ == '__main__':
	PORT = 5001
	app.run(host='0.0.0.0', debug=True, gevent=100, port=PORT)
	#app.run('0.0.0.0', PORT, ssl_context='adhoc')