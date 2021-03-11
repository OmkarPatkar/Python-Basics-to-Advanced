'''
BMI Calculator with Python
The body mass index is calculated by dividing an individual’s weight in kilograms by their height in meters, 
then dividing the answer again by their height. Now let’s see how to create a BMI calculator with Python:
'''

#take user inputs
height = float(input(' Enter your height in centimeters : '))
weight = float(input(' Enter your weight in kg : '))

height = height / 100

BMI = weight/(height * height)

#condition
print('your body mass index is :', BMI)
if(BMI > 0):
    if(BMI <= 16):
        print('you are severely underweight \n')
    elif(BMI <= 18.5):
        print('you are underweight \n')
    elif(BMI <= 25):
        print('you are healthy \n')
    elif(BMI <= 30):
        print('you are over weight \n')
    else:
        print('you are severely over weight \n')
else:
    ('enter valid details')