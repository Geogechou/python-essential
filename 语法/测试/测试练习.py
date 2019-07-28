import unittest
class Employee():
	def __init__(self,f_name,l_name,salary):
		self.firstName=f_name
		self.lastName=l_name
		self.salary=salary
	def give_raise(self,num=5000):
		self.salary+=num
class TestEmployee(unittest.TestCase):
	"""针对employee类的测试"""
	def setUp(self):
		"""
		创建一个对象，供测试使用
		"""
		self.emp=Employee('geoge','chow',1000)
	def test_give_default_raise(self):
		self.emp.give_raise()
		self.assertEqual(self.emp.salary,6000)	
	def test_give_custom_raise(self):
		self.emp.give_raise(1000)
		self.assertEqual(self.emp.salary,2000)
unittest.main()
