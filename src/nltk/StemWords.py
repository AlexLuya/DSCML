# -*- coding: utf-8 -*-

def stemWords(tokens,stemmer):
    stemmed=[]
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed