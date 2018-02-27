import datetime
import csv
class Logger:
	def __init__(self):
		self.fname = 'log_' + datetime.datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S') + '.csv'
	def log(self, msg):
		with open(self.fname, 'a') as f:
			writer = csv.writer(f)
			writer.writerow([datetime.datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S'), msg])
			f.close()