import requests
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print(page)

print(page.status_code)
print(page.content)
print(page.text)
print(dir(page))

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

print(soup.find_all('p'))
print(soup.find_all('p')[0].get_text())
print(soup.find('p'))
