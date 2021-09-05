import unittest
from city_functions import get_formatted_city

class CityTestClass(unittest.TestCase):
    '''Tests for city_functions.py'''

    def test_city_country_name(self):
        '''Does a name like 'Vilnius, Lithunia' work?'''
        formatted_city = get_formatted_city('vilnius', 'lithuania')
        self.assertEqual(formatted_city, 'Vilnius, Lithuania')

    def test_city_country_population(self):
        '''Does our function work when population is included?'''
        formatted_city = get_formatted_city('vilnius', 'lithuania', 
            population='544,000')
        self.assertEqual(formatted_city, 'Vilnius, Lithuania. '
            'Population: 544,000')

if __name__ == '__main__':
    unittest.main()
