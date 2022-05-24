#!/usr/bin/python3

import sys
from elasticsearch import Elasticsearch

es_host = "http://localhost:9200"

e1 = {
    "first_name" : "Iron",
    "last_name" : "Man",
    "age" : 27,
    "about" : "Hello world",
    "interests" : [ "sports", "music" ]
}

e2 = {
    "first_name" : "Michael",
    "last_name" : "Smith",
    "age" : 32,
    "about" : "I like to collect rock albums",
    "interests" : [ "music", "programming" ]
}

e3 = {
    "first_name" : "Douglas",
    "last_name" : "James",
    "age" : 15,
    "about" : "I like to build cabinets",
    "interests" : [ "forestry", "math" ]
}

e4 = {
    "first_name" : "Thor",
    "last_name" : "God",
    "age" : 44,
    "about" : "Love to play football",
    "interests" : [ "sports", "music" ]
}

if __name__ == '__main__':
    es = Elasticsearch(es_host)

    res = es.index(index='knu', id=1, document=e1)
    print(res)
    res = es.index(index='knu', id=2, document=e2)
    print(res)
    res = es.index(index='knu', id=3, document=e3)
    print(res)
    res = es.index(index='knu', id=4, document=e4)
    print(res)