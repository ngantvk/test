import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.dienmayxanh.com/')

soup = BeautifulSoup(response.text, 'html.parser')

soupFound = soup.find("div", {"id": "js-read__content"})

deleteTags = ['br', 'a', 'small', 'script', 'div', "html"]
for t in deleteTags:
    for e in soupFound.findAll(t):
        e.extract()

content = soupFound.contents
print(content)