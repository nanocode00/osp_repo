#!/usr/bin/python3
#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url1 = 'https://en.wikipedia.org/wiki/Web_crawler'
url2 = 'https://en.wikipedia.org/wiki/NoSQL'

def crawl_and_count(url):
    words, frequencies, search_list = list(), list(), list()
    search_tag = [ 'h1', 'h2', 'h3', 'p', 'table', 'ul', 'ol' ]
    res = requests.get(url)
    html = BeautifulSoup(res.content, "html.parser")
    content = html.find('div', id='content')
    for tag in search_tag:
        search_list += content.find_all(tag)
    for search_item in search_list:
        raw_line = str(search_item.get_text())
        line = str()

        in_square_bracket = 0
        for token in raw_line:
            if in_square_bracket > 0:
                if token == ']':
                    in_square_bracket -= 1
            else:
                if token == '[':
                    in_square_bracket += 1
                if not token.isalpha():
                    line += ' '
                else:
                    line += token.lower()
        
        for word in line.split():
            if not word in words:
                words.append(word)
                frequencies.append(1)
            else:
                frequencies[words.index(word)] += 1
    return { 'url' : url, 'words' : words, 'frequencies' : frequencies }

#data1 = crawl_and_count(url1)
#print(data1)
data2 = crawl_and_count(url2)
print(data2)