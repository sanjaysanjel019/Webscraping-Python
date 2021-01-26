from bs4 import BeautifulSoup

with open('index.html','r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    div_tags = soup.find_all('div', class_='card')
    for courses in div_tags:
        course_prices = courses.a.text.split()[-1]
        # print(course_prices)

        print(f'{course_prices} is pretty shit')
    
