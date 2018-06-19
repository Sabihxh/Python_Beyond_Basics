class TestClass(object):
	"""docstring for TestClass"""
	_private_a = 'Hello'
	__private = 'World'
		


i = TestClass()
print(i._private_a)
print(i._TestClass__private)
