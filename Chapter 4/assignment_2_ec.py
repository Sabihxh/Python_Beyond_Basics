
from datetime import datetime


class WriteFile(object):

	def __init__(self, filename, writer):
		self.filename = filename
		self.writer = writer()


	def write(self, value, linebreak='\n'):
		fh = open(self.filename, 'a')
		value = self.writer.get_line(value)
		value += linebreak
		fh.write(value)
		fh.close()


class LogFormatter(object):

	def get_line(self, value):
		date_value = datetime.now().strftime('%Y-%m-%d %H:%M')
		line = '{}\t{}'.format(date_value, value)
		return line


class CSVFormatter(object):

	def get_line(self, list_values, delimeter=','):
		for i, value in enumerate(list_values):
			if delimeter in value:
				list_values[i] = '"%s"' % value
		
		line = delimeter.join(list_values)
		return line