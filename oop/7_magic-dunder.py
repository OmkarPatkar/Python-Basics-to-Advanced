# magic or dunder methods

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

    # we create a classmethod when we don't want to pass the whole object
    # to the function and just want to change few variables
    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount

    # magic/ dunder method
    # we can not add two objects directly so we create a dunder method
    def __add__(self, other):
        # adding two employees salary
        return self.salary + other.salary

    # magic / dunder method
    # overriding repr dunder method
    def __repr__(self):
        return f'Employee({self.fname}, {self.lname}, {self.salary})'

    # magic / dunder method
    # overriding str dunder method
    def __str__(self):
        return f'The name of Employee is {self.fname}'

# checking no_of _emp at start
print(f'no_of_emp: {Employee.no_of_emp}')

# create objects for employee class to hold the values
emp1 = Employee('don', 'bose', 40000)
emp2 = Employee('tim', 'blue', 50000)

# overriding repr dunder method
print(f'overriding repr dunder method: {repr(emp2)}')

# overriding str dunder method
print(f'overriding str dunder method: {emp1}')

# checking no_of _emp after objects creation
print(f'no_of_emp after objects creation: {Employee.no_of_emp}')

# print the values
print(f'salary of employee 1: {emp1.salary}\nsalary of employee 2: {emp2.salary}')

# using magic/ dunder method to add salary of two employees
print(f'salary of employee 1 + employee 2: {emp1+emp2}')

# run additional function for employee class objects
Employee.change_increment(4)
emp1.increase()

# print the values
print(f'salary of employee 1 after increment: {emp1.salary}')

