# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 08:14:38 2016

@author: alex
"""

from nltk.corpus import sinica_treebank

sents=sinica_treebank.parsed_sents()[15]

print type(sents)

sents.draw()
