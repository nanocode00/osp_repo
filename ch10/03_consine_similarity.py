#!/usr/bin/python3
from lib2to3.pgen2 import token
from multiprocessing import Semaphore
import numpy
from nltk import word_tokenize

word_d = {}
sent_list = []

def process_new_sentence(s):
    sent_list.append(s)
    toknized = word_tokenize(s)
    for word in toknized:
        if word not in word_d.keys():
            word_d[word] = 0
        word_d[word] += 1

def make_vector(i):
    v = []
    s = sent_list[i]
    tokenized = word_tokenize(s)
    for w in word_d.keys():
        val = 0
        for t in tokenized:
            if t == w:
                val += 1
        v.append(val)
    return v

if __name__ == '__main__':
    process_new_sentence("yesterday u saw you study in the house")
    process_new_sentence("yesterday u saw you study in the school")
    
    #print(sent_list[0])
    #print(make_vector(0))
    #print(sent_list[1])
    #print(make_vector(1))

    v1 = make_vector(0)
    v2 = make_vector(1)

    dotpro = numpy.dot(v1, v2)
    cossimil = dotpro / (numpy.linalg.norm(v1) * numpy.linalg.norm(v2))

    print("dot product =", dotpro)
    print("cos similarity =", cossimil)