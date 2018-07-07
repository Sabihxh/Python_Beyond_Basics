
class ConfigKeyError(Exception):

	def __init__(self, dict_obj, key):
		self._key = key
		self._keys = dict_obj.keys()
		self._avail_keys = ', '.join(map(str, self._keys))
		

	def __str__(self):
		params = (self._key, self._avail_keys)
		msg = "Key \"{0}\" not found. Available keys: ({1})".format(*params)
		return msg