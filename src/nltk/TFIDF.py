# -*- coding: utf-8 -*-

from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
import csv

episodes=defaultdict(list)

with open("/home/alex/data/sentences.csv") as sentencs:
    reader=csv.reader(sentencs)
#     ignore titles
    reader.next()
    
    for row in reader:
        episodes[row[1]].append(row[4])
        
    for episode_id,text in episodes.iteritems():
        episodes[episode_id]="".join(text)    
        
corpus=[]
for id,episode in sorted(episodes.iteritems(),key=lambda t:int(t[0])):
    corpus.append(episode)        
    
tf = TfidfVectorizer(analyzer='word', ngram_range=(1,3), min_df = 0, stop_words = 'english')

tfidf_matrix =  tf.fit_transform(corpus)
feature_names = tf.get_feature_names() 