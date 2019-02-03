import unittest

def get_formatted_city(city,country,population=""):
	if population:
		return city.title()+","+country.title()+"-population "+population
	else:	
		return city.title()+","+country.title()
class test_city_country(unittest.TestCase):
	"""测试 formatted_city()函数"""
	def test_city_country(self):
		formatted_city=get_formatted_city("london","british")
		self.assertEqual(formatted_city,"London,British")
	def test_city_country_population(self):
		formatted_city=get_formatted_city("london","british","1000w")
		self.assertEqual(formatted_city,"London,British-population 1000w")
		
unittest.main()
