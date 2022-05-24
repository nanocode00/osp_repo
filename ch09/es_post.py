#!/usr/bin/python3
#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch

url1 = 'https://en.wikipedia.org/wiki/Web_crawler'
url2 = 'https://en.wikipedia.org/wiki/NoSQL'
es_host = 'http://localhost:9200'
index_web = 'web'

def crawl_and_count(url):
    words, frequencies, search_list = list(), list(), list()
    search_tag = [ 'h1', 'h2', 'h3', 'h4', 'h5', 'p', 'table', 'ul', 'ol' ]
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

if __name__ == '__main__':
    es = Elasticsearch(es_host)

    if not es.indices.exists(index=index_web):
        es.indices.create(index=index_web)
    
    doc1 = crawl_and_count(url1)
    res = es.index(index=index_web, id=1, document=doc1)

    doc2 = crawl_and_count(url2)
    res = es.index(index=index_web, id=2, document=doc2)

    print(es.get(index=index_web, id=1))