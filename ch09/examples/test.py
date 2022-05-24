#!/usr/bin/python3

import sys
from elasticsearch import Elasticsearch

es_host="http://localhost:9200"

if __name__ == '__main__':
    es = Elasticsearch(es_host)

    query = { "query" : { "bool" : { "must" : [ { "match" : { "title" : "Interstellar"} } ] } } }

    while True:
        try:
            docs = es.search(index='movies', body=query, size=10)
            break
        except Exception as e:
            print(1)
            continue
    
    if docs['hits']['total']['value'] > 0:
        for doc in docs['hits']['hits']:
            print(doc['_source'])