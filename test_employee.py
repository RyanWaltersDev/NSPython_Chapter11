import unittest
from employee import Employee

class TestEmployeeClass(unittest.TestCase):
    '''
    Test raise and format methods from Employee class in employee.py
    '''

    def setUp(self):
        '''Initialize employee for method tests'''
        self.employee = Employee('jim', 'halpert', 50000)

    def test_formatted_name(self):
        '''Check to make sure name is correctly formatted'''
        formatted_name = self.employee.format_employee()
        self.assertEqual(formatted_name, 'Jim Halpert: $50000')

    def test_give_default_raise(self):
        '''Check to make sure salary is raised by 5000'''
        new_salary = self.employee.give_raise()
        self.assertEqual(new_salary, 55000)

    def test_give_custom_raise(self):
        '''Check to make sure salary can be raised custom amount'''
        new_salary = self.employee.give_raise(4321)
        self.assertEqual(new_salary, 54321)


if __name__ == '__main__':
    unittest.main()
