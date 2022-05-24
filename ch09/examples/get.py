#!/usr/bin.python3

import sys
from elasticsearch import Elasticsearch

es_host = "http://localhost:9200"

if __name__ == '__main__':
    ex = Elasticsearch(es_host)

    index_list = []

    index_list = ex.indices.get(index='*')
    index_list = sorted(index_list, reverse=True)

    print(index_list)