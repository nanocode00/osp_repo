#!/usr/bin/python3

import sys
from elasticsearch import Elasticsearch

url1 = 'https://en.wikipedia.org/wiki/Web_crawler'
url2 = 'https://en.wikipedia.org/wiki/NoSQL'
es_host = 'http://localhost:9200'
index_web = 'web'

if __name__ == '__main__':
    es = Elasticsearch(es_host)

    query = { "query" : { "bool" : { "filter" : [ { "match" : { "url.keyword" : url1 } } ] } } }
    print(query)
    while True:
        try:
            docs = es.search(index=index_web, body=query)
            break
        except Exception as e:
            print(1)
            continue
    
    if docs['hits']['total']['value'] > 0:
        print(docs['hits']['hits'][0]['_id'])
        print(type(docs['hits']['hits'][0]['_id']))