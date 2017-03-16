# -*- coding: utf-8 -*-

import nltk
import string


def getTokens(f):
    with open(f,'r') as f:
        text=f.read()
        lowers=text.lower()
        no_punctuation=lowers.translate(None,string.punctuation)
        
        return nltk.word_tokenize(no_punctuation)
