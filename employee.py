class Employee():
    '''A simple model of an employee name and salary'''

    def __init__(self, first_name, last_name, salary):
        '''Initialize employee's attributes'''
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def format_employee(self):
        '''List the employee's name and salary'''
        formatted_employee = (f"{self.first_name.title()} "
            f"{self.last_name.title()}: ${self.salary}")
        return formatted_employee

    def give_raise(self, salary_raise=5000):
        '''Give employee a raise with 5000 as the default'''
        self.salary += salary_raise
        return self.salary
