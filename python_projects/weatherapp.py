# import libraries
from bs4 import BeautifulSoup
import requests

# accept the city name
city = input('Enter the city name to know its weather: ')
city = f"Temperature in {city}"
# search the city on web
url = f'https://www.google.com/search?&q={city}'

# get the data for the provided city
r = requests.get(url)

# parse the data
s = BeautifulSoup(r.text, 'html.parser')

# parse the temperature from the data
temp = s.find('div', class_ = 'BNeawe').text
# condition to get more accurate results
if len(temp) == 4:
    print(f'{city} is {temp}')
else:
    print('Enter valid city.')

