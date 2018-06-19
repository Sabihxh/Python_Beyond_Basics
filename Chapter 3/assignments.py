class MaxSizelist(object):

	def __init__(self, max_size):
		self.max_size = max_size
		self.user_list = []

	
	def push(self, item):
		self.user_list.append(item)
		if len(self.user_list) > self.max_size:
			self.user_list.pop(0)


	def get_list(self):
		return self.user_list


a = MaxSizelist(3)
a.push('hey')
a.push('I')
a.push('am')
a.push('here')

print(a.get_list())

b = MaxSizelist(1)
b.push('hey')
b.push('I')
b.push('am')
b.push('here')

print(b.get_list())



