# class variables and instance variables

# class is basically a blue print or a template in which we can modify
# or add new functionality
class Employee:

    # class variable
    increment = 1.5
    no_of_emp = 0

    # we create a constructor __init__, it is executed as we run our program
    def __init__(self, fname, lname, salary):
        # instance variables
        self.fname = fname
        self.lname = lname
        self.salary = salary
        # class variable
        Employee.no_of_emp += 1

    def increase(self):
        # in oop we can either access the instance or the class variable
        # it first searches for instance variable and then class variable (increment)
        self.salary = int(self.salary * self.increment)

# checking no_of _emp at start
print(f'no_of_emp: {Employee.no_of_emp}')

# create objects to hold the values
emp1 = Employee('don', 'bose', 40000)
emp2 = Employee('tim', 'blue', 50000)

# checking no_of _emp after objects creation
print(f'no_of_emp after objects creation: {Employee.no_of_emp}')

# print the values
print(f'salary of employee 1: {emp1.salary}\nsalary of employee 2: {emp2.salary}')

# run additional function
emp1.increase()

# print the values
print(f'salary of employee 1 after increment: {emp1.salary}')

# to check for all the instance variables
print(f'emp1 instance variables: {emp1.__dict__}')

# we can add an instance variable
emp1.increment = 10

# to check for all the instance variables
print(f'emp1 instance variables after adding an instance variable: {emp1.__dict__}')

# to check for all the class variables
print(f'Employee class variables: {Employee.__dict__}')