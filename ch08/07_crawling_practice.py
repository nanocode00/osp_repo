#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

if __name__ == '__main__':

    url = u'https://ko.wikipedia.org/wiki/웹_크롤러'
    res = requests.get(url)

    html = BeautifulSoup(res.content, "html.parser")

    html_title = html.find("title")

    html_body = html.find(attrs={'class':'mw-parser-output'})

    title = html_title.text
    body = html_body.find('p').text

    print("title:", title)
    print("body:", body)