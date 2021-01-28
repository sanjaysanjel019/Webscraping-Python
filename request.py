from bs4 import BeautifulSoup
import requests

html_content = requests.get(
    'https://dukeenergy.wd1.myworkdayjobs.com/search').text
soup = BeautifulSoup(html_content, 'lxml')
# print(soup)
h4_tags = soup.find_all('div')
for title in h4_tags:
    print(title)
