# class inheritance

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

# checking no_of _emp at start
print(f'no_of_emp: {Employee.no_of_emp}')

# create objects for employee class to hold the values
emp1 = Employee('don', 'bose', 40000)
emp2 = Employee('tim', 'blue', 50000)

# checking no_of _emp after objects creation
print(f'no_of_emp after objects creation: {Employee.no_of_emp}')

# print the values
print(f'salary of employee 1: {emp1.salary}\nsalary of employee 2: {emp2.salary}')

# run additional function for employee class objects
Employee.change_increment(4)
emp1.increase()

# print the values
print(f'salary of employee 1 after increment: {emp1.salary}')

print()
print()
print('INHERITANCE IN PYTHON')
print('*' * 50)
"""
In inheritance we can utilies the parent class variables 
and add some extra functionality to our new class.
"""
# inheriting from Employee class
class programmer(Employee):
    def __init__(self, fname, lname, salary, prolang, exp):
        # super is a constructor that calls and inherit the properties from parent class
        super(programmer, self).__init__(fname, lname, salary)
        # instance variables of programmer class
        self.prolang = prolang
        self.exp = exp

    # we overload the increase function in employee class and add an increament of 0.2 to the salary
    def increase(self):
        self.salary = int(self.salary * (self.increment + 0.2))

# create objects for programmer class to hold the values
pro1 = programmer('doni', 'jobose', 20, 'python', '3 yrs')

# print the values
print(f'experience of programmer 1: {pro1.exp}')
print(f'salary of programmer 1: {pro1.salary}')

# run additional function for programmer class objects
programmer.change_increment(4)
pro1.increase()

# print the values
print(f'salary of programmer 1 after increment: {pro1.salary}')

