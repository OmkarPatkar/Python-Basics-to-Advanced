# static methods

# class is basically a blue print or a template in which we can modify
# or add new functionality
class Employee:
    # we create a constructor __init__
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    # independent function
    # staticmethods are used when we don't want or need to pass the
    # class or instance as an argument to the function
    @staticmethod
    def isopen(day):
        if day == 'sunday' or day == 'Sunday':
            return False
        else:
            return True

# create objects to hold the values
emp1 = Employee('don', 'bose', 40000)
emp2 = Employee('tim', 'blue', 60000)

# print the values
print(f'name of employee 1: {emp1.fname}\nname of employee 2: {emp2.fname}')
print(f'running isopen on class: {Employee.isopen("sunday")}')
print(f'running isopen on instance: {emp2.isopen("monday")}')
