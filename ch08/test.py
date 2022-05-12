import re
import requests
from bs4 import BeautifulSoup

url1 = 'https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States'
url2 = 'https://finance.naver.com/sise/'

def crawl_url1():
    res = requests.get(url1)
    html = BeautifulSoup(res.content, "html.parser")
    table = html.find('table', class_='wikitable')
    link = table.select('b a')
    title = list(map(lambda x: x.get_text(), link))
    return title

def crawl_url2():
    res = requests.get(url2)
    html = BeautifulSoup(res.content, "html.parser")

    KOSPI = []
    change = html.find(id='KOSPI_change').get_text().split()
    KOSPI.append(html.find(id='KOSPI_now').get_text())
    KOSPI.append(change[0])
    KOSPI.append(change[1][0:-2])

    KOSDAQ = []
    change = html.find(id='KOSDAQ_change').get_text().split()
    KOSDAQ.append(html.find(id='KOSDAQ_now').get_text())
    KOSDAQ.append(change[0])
    KOSDAQ.append(change[1][0:-2])

    KPI200 = []
    change = html.find(id='KPI200_change').get_text().split()
    KPI200.append(html.find(id='KPI200_now').get_text())
    KPI200.append(change[0])
    KPI200.append(change[1][0:-2])

    return [KOSPI, KOSDAQ, KPI200]

names = crawl_url1()
print(names)
sise = crawl_url2()
print(sise)