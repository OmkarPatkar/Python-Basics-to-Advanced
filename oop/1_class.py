# a simple class creation

# class is basically a blue print or a template in which we can modify
# or add new functionality
class Employee:
    # we create a constructor __init__
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

# create objects to hold the values
emp1 = Employee('don', 'bose', 40000)
emp2 = Employee('tim', 'blue', 60000)

# print the values
print(f'name of employee 1: {emp1.fname}\nname of employee 2: {emp2.fname}')