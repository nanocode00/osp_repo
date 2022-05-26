#!/usr/bin/python3

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

if __name__ == '__main__':
    mysent = 'The subject of Knowledge Discovery and Data Mining concerns the extraction of useful information from data. Since this is also the essence of many subareas of computer science, as well as the field of statistics, KDD can be said to lie at the intersection of statistics, machine learning, data bases, pattern recognition, information retrieval and artificial intelligence.'
    swlist = []
    for sw in stopwords.words("english"):
        swlist.append(sw)
    tokenized = word_tokenize(mysent)

    result = []
    for w in tokenized:
        if w not in swlist:
            result.append(w)
    
    print(len(tokenized))
    print(len(result))