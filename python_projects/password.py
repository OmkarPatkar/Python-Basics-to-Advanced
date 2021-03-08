#import libraries
import random

#accept a num for the length of the password
passlen = int(input('Enter the length of the password: '))

#characters to create the password
s = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+'

#create the password
password = ''.join(random.sample(s, passlen))

print(f'your password is {password}')
