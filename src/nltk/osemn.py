# -*- coding: utf-8 -*-
import os,re

alice=open('/home/alex/data/alice.txt','r').read().replace('\r\n','').lower()

stopPattern='\.|\?|\!'

stns=re.split(stopPattern,alice)

for i,sntnc in enumerate(stns):
    if 'alice' in sntnc and 'drink' in sntnc:
        print i,sntnc,'\n' 
