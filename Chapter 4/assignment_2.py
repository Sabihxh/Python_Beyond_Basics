import abc
from datetime import datetime

class WriteFile(object):
	
	__metaclass__ = abc.ABCMeta

	def __init__(self, filename):
		self.filename = filename
		
	@abc.abstractmethod
	def write(self, value):
		return

	def writeline(self, value, linebreak='\n'):
		fh = open(self.filename, 'a')
		fh.write(value + linebreak)
		fh.close()


class LogFile(WriteFile):

	def write(self, value):
		date_value = datetime.now().strftime('%Y-%m-%d %H:%M')
		value = '{}\t{}'.format(date_value, value)
		self.writeline(value)


class DelimFile(WriteFile):

	def __init__(self, filename, delim=','):
		super(DelimFile, self).__init__(filename)
		self.delim = delim


	def write(self, list_values):
		for i, value in enumerate(list_values):
			if self.delim in value:
				list_values[i] = '"%s"' % value

		value = self.delim.join(list_values)
		self.writeline(value)


log = LogFile('log.txt')
log.write('Heyyy')


mydelim = DelimFile('data.csv')
mydelim.write(['Heyyy', 'I have, something', 'incredible'])
mydelim.write(['Heyyy', 'I have, something LOOOOL', 'incredible'])


# -----------------------------------

from assignment_2_ec import WriteFile, LogFormatter, CSVFormatter


writecsv = WriteFile('data2.txt', CSVFormatter)
writecsv.write(['Heyyy', 'I have, something', 'incredible'])
writecsv.write(['Heyyy', 'I have, something', 'nice'])
writecsv.write(['Heyyy', 'I have, something', 'great'])


writelog = WriteFile('log2.txt', LogFormatter)
writelog.write('HEY! This is my log file...0')
writelog.write('HEY! This is my log file...1')
writelog.write('HEY! This is my log file...2')
writelog.write('HEY! This is my log file...3')





