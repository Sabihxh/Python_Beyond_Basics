import sys
# from assignment_3 import ConfigDict

class ConfigDict(dict):
	"""docstring for ConfigDict"""
	def __init__(self, filepath):
		config = open(filepath)

		config_dict = {}
		for line in config:
			key_value = line.split('=')
			key = key_value[0]
			value = key_value[1]
			config_dict[key] = value.strip()

		print(config_dict)


	def __setitem__(self, key, val):
		dict.__setitem__(self, key, val)
		

cd = ConfigDict('config.txt')


# if len(sys.argv) == 3:

#     key = sys.argv[1]
#     value = sys.argv[2]
#     print('writing data:  {0}, {1}'.format(key, value))

#     cd[key] = value

# else:

#     print('reading data')
#     for key in cd.keys():
#         print('   {0} = {1}'.format(key, cd[key]))





