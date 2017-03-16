# -*- coding: utf-8 -*-

from nltk.corpus import stopwords

def removeStopWords(tokens):
    return [w for w in tokens if not w in stopwords.words('english')]
