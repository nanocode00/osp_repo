#!/usr/bin/python3

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

if __name__ == '__main__':
    swlist = []
    for sw in stopwords.words("english"):
        swlist.append(sw)
        print(sw)