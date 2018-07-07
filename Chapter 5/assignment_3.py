import sys
import os
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
		with open(self._filepath, 'w') as fh:
			for key, value in self.items():
				fh.write('{0}={1}\n'.format(key, value))



cd = ConfigDict('config.txt')

if len(sys.argv) == 3:

    key = sys.argv[1]
    value = sys.argv[2]
    print('writing data:  {0}, {1}'.format(key, value))

    cd[key] = value

else:

    print('reading data')
    for key in cd.keys():
        print('   {0} = {1}'.format(key, cd[key]))





