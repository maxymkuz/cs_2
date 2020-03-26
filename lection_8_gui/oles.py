import requests
import re
from bs4 import BeautifulSoup

# GET request to a url
rget = requests.get(
	            'https://www.itjobswatch.co.uk/jobs/uk/python%20developer.do')
content = rget.content

# Create a soup object
soup = BeautifulSoup(content, 'html.parser')
main_content = soup.find_all('td',
	                         attrs = {'class': 'tabRelatedGroupsContainer'})

r = [row.get_text() for row in main_content][:2]

print(r[0].split())
print(r[1].split())

# Pattern to match IT Skills name
name_pattern = re.compile(r'^([A-Z]{1}.+)', flags = re.M)
names = name_pattern.findall(r[0])
print(names)

# Pattern to extract proportion
proportion_pattern = re.compile(r'(\d{2,3}\.\d{2})')
proportion = proportion_pattern.findall(r[0])
print(proportion)

# Pattern to extract absolute number IT Skills
absolute_number_pattern = re.compile(r'\d?,?\d{3}')
absolute_number = absolute_number_pattern.findall(r[0])
print(absolute_number)

# DataFrame creation

# Vizualization