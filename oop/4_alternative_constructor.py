# Class Methods As Alternative Constructor

# class is basically a blue print or a template in which we can modify
# or add new functionality
class Employee:

    # class variable
    no_of_emp = 0

    # we create a constructor __init__, it is executed as we run our program
    def __init__(self, fname, lname, salary):
        # instance variables
        self.fname = fname
        self.lname = lname
        self.salary = salary
        # class variable
        Employee.no_of_emp += 1

    # we can use Class Methods As Alternative Constructor
    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split('-')
        return cls(fname, lname, salary)

# checking no_of _emp at start
print(f'no_of_emp: {Employee.no_of_emp}')

# create objects to hold the values
emp1 = Employee('don', 'bose', 40000)
emp2 = Employee('tim', 'blue', 50000)

# create object and provide values for alternative constructor
emp3 = Employee.from_str('led-jop-80000')

# print the values
print(f'''name of employee 3: {emp3.fname}',\nlname of employee 3: {emp3.lname}, \nsalary of employee 3: {emp3.salary}''')

# checking no_of _emp after objects creation
print(f'no_of_emp after objects creation: {Employee.no_of_emp}')
