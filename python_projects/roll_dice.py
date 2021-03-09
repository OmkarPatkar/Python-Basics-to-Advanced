# import libraries
import random

# range for rolling the dice
min = 1
max = 6

#take user input
roll_dice = input('Wanna roll the dices? (yes/y)\n')

#create a condition
while roll_dice == 'yes' or roll_dice == 'y':
    print('Rolling the dices...')
    print('The values are...')
    
    #1st dice value
    print(random.randint(min, max))
    
    #2nd dice value
    print(random.randint(min, max))
    
    print('*' * 50)
    roll_dice = input('Roll dice again? (yes/y)\n')