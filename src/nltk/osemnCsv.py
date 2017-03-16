# -*- coding: utf-8 -*-
# This is a comment
# This is another comment

import csv

with open('../data/example.csv') as f:
    for line in csv.reader(row for row in f if not row.startswith('#')):
        name,wt,ht=line
        wt,ht=map(float,(wt,ht))
        print 'BMI of %s=%.2f' % (name,wt/(ht*ht))