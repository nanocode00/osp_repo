#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, jsonify, request
from flask import redirect, url_for

url1 = 'https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States'
url2 = 'https://finance.naver.com/sise/'

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        url = request.form['url']
        if url == url1:
            return redirect(url_for('res_url1'))
        elif url == url2:
            return redirect(url_for('res_url2'))
        else:
            res = requests.get(url)
            html = BeautifulSoup(res.content, "html.parser").prettify()
            return render_template("result.html", parsed_result=html)

@app.route('/result/url1')
def res_url1():
    res = requests.get(url1)
    html = BeautifulSoup(res.content, "html.parser")
    table = html.find('table', class_='wikitable')
    link = table.select('b a')
    names = list(map(lambda x: x.get_text(), link))
    return render_template("result_url1.html", names=names)

@app.route('/result/url2')
def res_url2():
    res = requests.get(url2)
    html = BeautifulSoup(res.content, "html.parser")

    kospi = []
    change = html.find(id='KOSPI_change').get_text().split()
    kospi.append(html.find(id='KOSPI_now').get_text())
    kospi.append(change[0])
    kospi.append(change[1][0:-2])

    kosdaq = []
    change = html.find(id='KOSDAQ_change').get_text().split()
    kosdaq.append(html.find(id='KOSDAQ_now').get_text())
    kosdaq.append(change[0])
    kosdaq.append(change[1][0:-2])

    kpi200 = []
    change = html.find(id='KPI200_change').get_text().split()
    kpi200.append(html.find(id='KPI200_now').get_text())
    kpi200.append(change[0])
    kpi200.append(change[1][0:-2])

    return render_template("result_url2.html", kospi=kospi, kosdaq=kosdaq, kpi200=kpi200)

if __name__ == '__main__':
    app.run()