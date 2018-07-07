import os
import sys
import pickle

class ConfigKeyError(Exception):
	
	def __init__(self, this, key):
		self.key = key
		self.keys = this.keys()

	def __str__(self):
		return "key '{0}' not found. Available keys ({1})".format(self.key, ', '.join(self.keys))


class ConfigPickleDict(dict):

	config_dir = '/Users/yuartcha/Desktop/config'

	def __init__(self, config_name):
		
		self._config_path = os.path.join(ConfigPickleDict.config_dir, config_name + '.pickle')
		
		if not os.path.isfile(self._config_path):
			with open(self._config_path, 'w') as fh:
				pickle.dump({}, fh)

		with open(self._config_path) as fh:
			pkl = pickle.load(fh)
			self.update(pkl)


	def __getitem__(self, key):
		if key not in self:
			raise ConfigKeyError(self, key)
		return dict.__getitem__(self, key)


	def __setitem__(self, key, val):
		dict.__setitem__(self, key, val)
		with open(self._config_path, 'w') as fh:
			pickle.dump(self, fh)
