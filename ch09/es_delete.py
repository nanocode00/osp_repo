#!/usr/bin/python3
#-*- coding: utf-8 -*-

from elasticsearch import Elasticsearch

es_host = 'http://localhost:9200'
index_web = 'web'

if __name__ == '__main__':
    es = Elasticsearch(es_host)

    if es.indices.exists(index=index_web):
        es.indices.delete(index=index_web, ignore=[400, 404])
