#!/usr/bin/python3
#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch
import elastic_transport

url1 = 'https://en.wikipedia.org/wiki/Web_crawler'
url2 = 'https://en.wikipedia.org/wiki/NoSQL'
es_host = 'http://localhost:9200'
index_web = 'web'

if __name__ == '__main__':
    es = Elasticsearch(es_host)

    try:
        if not es.indices.exists(index=index_web):
            es.indices.create(index=index_web)
    except elastic_transport.ConnectionError as e:
        print(e)
        exit()
    n = es.count(index=index_web)['count']

    for i in range(1, n + 1):
        print(es.get(index=index_web, id=i)['_source'])

