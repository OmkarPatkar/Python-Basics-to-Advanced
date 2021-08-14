# Property Decorators, setters, deleters

# class is basically a blue print or a template in which we can modify
# or add new functionality
class Employee:

    # we create a constructor __init__, it is executed as we run our program
    def __init__(self, fname, lname, salary):
        # instance variables
        self.fname = fname
        self.lname = lname
        self.salary = salary

    # using property decorator we can use a function as an attribute
    @property
    def email(self):
        if self.fname == None:
            return 'Email not set.'
        else:
            return self.fname + '.' + self.lname + '@gmail.com'

    # Setter method to set the values
    @email.setter
    def email(self, given_email):
        name_list = given_email.split('@')[0].split('.')
        self.fname = name_list[0]
        self.lname = name_list[1]

    # Deleter method to delete values
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

if __name__ == '__main__':
    # create objects for employee class to hold the values
    emp1 = Employee('don', 'bose', 40000)
    emp2 = Employee('tim', 'blue', 50000)

    # accessing data through the Property Decorator
    print(f'emails : 1:{emp1.email}, 2:{emp2.email}')

    # now if we change the last name
    emp2.lname = 'ban'
    print(f'after changing lname: {emp2.email}')

    # if we change or set the email, we'll use Setter Method above
    emp2.email = 'ban.tim@gamil.com'
    print(f'setting the email: {emp2.email}')

    # deleting the email using Deleter Method
    del emp2.email
    print(f'Trying to print deleted email: {emp2.email}')





