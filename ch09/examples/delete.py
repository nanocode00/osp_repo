#!/usr/bin/python3

import sys
from elasticsearch import Elasticsearch

es_host = "http://localhost:9200"

if __name__ == '__main__':
    es = Elasticsearch(es_host)

    es.indices.delete(index='knu', ignore=[400, 404])