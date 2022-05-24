#!/usr/bin/python3
#-*- coding: utf-8 -*-

from pydoc import source_synopsis
import re
import elastic_transport
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, jsonify, request
from flask import redirect, url_for
from elasticsearch import Elasticsearch

url1 = 'https://en.wikipedia.org/wiki/Web_crawler'
url2 = 'https://en.wikipedia.org/wiki/NoSQL'
es_host = 'http://localhost:9200'
index_web = 'web'

def crawl_and_count(url):
    words, frequencies, search_list = list(), list(), list()
    tag_to_search = [ 'h1', 'h2', 'h3', 'h4', 'h5', 'p', 'table' ]

    res = requests.get(url)
    if res.status_code != 200:
        return None
    html = BeautifulSoup(res.content, "html.parser")
    if url == url1 or url == url2:
        content = html.find('div', id='content')
    else:
        content = html
    for tag in tag_to_search:
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

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        url = request.form['url']
        data = crawl_and_count(url)

        query = { "query" : { "bool" : { "filter" : [ { "match" : { "url.keyword" : url } } ] } } }
        docs = es.search(index=index_web, body=query)

        if data == None:
            if docs['hits']['total']['value'] > 0:
                data = docs['hits']['hits']['_source']
            else:
                return 'No connection and stored data'
        else:
            if docs['hits']['total']['value'] > 0:
                id = int(docs['hits']['hits'][0]['_id'])
            else:
                id = es.count(index=index_web)['count'] + 1
            es.index(index=index_web, id=id, document=data)
        return render_template("result.html", data=data)
        
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    es = Elasticsearch(es_host)

    try:
        if not es.indices.exists(index=index_web):
            es.indices.create(index=index_web)
    except elastic_transport.ConnectionError as e:
        print('Elasticsearch is not running!')
        print(e)
        exit()
    
    app.run()