import sys
import os
from error_handler import ConfigKeyError
# from assignment_3 import ConfigDict

class ConfigDict(dict):
	
	def __init__(self, filepath):

		self._filepath = filepath
		if os.path.exists(self._filepath):
			with open(self._filepath) as f:
				for line in f:
					line = line.rstrip()
					key, value = line.split('=', 1)
					dict.__setitem__(self, key, value)


	def __setitem__(self, key, val):

		dict.__setitem__(self, key, val)
		try:
			with open(self._filepath, 'w') as fh:
				for key, value in self.items():
					fh.write('{0}={1}\n'.format(key, value))
		except IOError as e:
			raise IOError("Please enter a valid filename/filepath")



	def __getitem__(self, key):

		if key not in self:
			raise ConfigKeyError(self, key)
		return dict.__getitem__(self, key)


