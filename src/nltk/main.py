# -*- coding: utf-8 -*-
from collections import Counter
from nltk.stem.porter import *
import StemWords
import os
import string
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

#tokens=GetTokens.getTokens("/home/alex/data/shakes.txt")
#
#print Counter(tokens).most_common(10)
#
#filtered=RemoveStopWords.removeStopWords(tokens)
#
#stemmed=StemWords.stemWords(filtered,PorterStemmer())

def tokenize(txt):
    return StemWords.stemWords(nltk.word_tokenize(txt),PorterStemmer())
    
    
#print Counter(tokenize("/home/alex/data/shakes.txt")).most_common(10)

no_punctuations={}

for subdir,dirs,files in os.walk('/home/alex/data/shakes'):
    for f in files:
        file_path=subdir+os.path.sep+f
        lowers=open(file_path,'r').read().lower()
        no_punctuations[file]=lowers.translate(None,string.punctuation)


tfidf=TfidfVectorizer(tokenizer=tokenize,stop_words='english')

tfs=tfidf.fit_transform(no_punctuations.values())

print tfs