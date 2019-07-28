import unittest

class AnnoymousSurvey():
	"""收集匿名调查问卷的答案"""
	
	def __init__(self,question):
		"""存储一个问题，并为存储答案做准备"""
		self.question=question
		self.response=[]
	def	show_question(self):
		"""显示调查问卷"""
		print(self.question)
	def store_response(self,new_response):
		"""存储单份调查问卷"""
		self.response.append(new_response)
	def show_result(self):
		"""显示收集到的所有答案"""
		print("Survey results:")
		for response in self.response:
			print(response)

class TestAnonymousSurvey(unittest.TestCase):
	"""针对AnnoymouSurvey类的测试"""
	def setUp(self):
		"""创建一个调查对象和一组答案，供使用的测试方法使用"""
		question="what language did you first learn to speak"
		self.my_survey=AnnoymousSurvey(question)
		self.responses=['English','Spanish','Mandarin']
		
	def test_store_single_response(self):
		self.my_survey.store_response('English')
		self.assertIn(self.responses[0],self.my_survey.response)
		
	def test_store_three_response(self):
		for response in self.responses:
			self.my_survey.store_response(response)
		for v in self.responses:
			self.assertIn(v,self.my_survey.response)
		
unittest.main()		
