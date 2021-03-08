#import libraries
from datetime import datetime
from playsound import playsound

#take user input
alarm_time = input("Enter the time of alarm to be set: HH:MM:SS:PP (01:02:03:PM)\n")

#store the values
hour = alarm_time[0:2]
minute = alarm_time[3:5]
second = alarm_time[6:8]
period = alarm_time[9:11].upper()

print('Setting up alarm...')
while True:
    now = datetime.now()
    current_hour = now.strftime('%I')
    current_minute = now.strftime('%M')
    current_second = now.strftime('%S')
    current_period = now.strftime('%p')
    if(period == current_period):
        if(hour == current_hour):
            if(minute == current_minute):
                if(second == current_second):
                    print('Wake Up!')
                    playsound('Bell.mp3')
                    break