k# -*- coding: utf-8 -*-
#from nltk.corpus import sinica_treebank
#
#sinica_text = nltk.Text(sinica_treebank.words())
#
#sinica_treebank.words()
#
#sinica_treebank.tagged_words()
#
#sinica_treebank.parsed_sents()[15].draw()

#from nltk.parse import stanford
#s = '你好'.decode('utf-8')
#
#print s
#parser = stanford.StanfordParser(path_to_jar='/home/alex/Software/nltk/stanford-parser.jar',path_to_models_jar='/home/alex/Software/nltk/stanford-parser-3.6.0-models.jar')
#print parser.raw_parse_sents(s)


from nltk.tokenize.stanford_segmenter import StanfordSegmenter
import os

segementerPath='/media/Backup/nltk/stanford-segmenter-2015-12-09/'
os.environ['CLASSPATH'] = segementerPath

segmenter = StanfordSegmenter(path_to_jar=segementerPath+'stanford-segmenter-3.6.0.jar',path_to_sihan_corpora_dict=segementerPath+'data',path_to_model=segementerPath+'data/pku.gz',path_to_dict=segementerPath+'data/dict-chris6.ser.gz')
sentence = u"这是斯坦福中文分词器测试"
segmenter.segment(sentence)
#segmenter.segment_file('test.simp.utf8')
#outfile = open('outfile', 'w')
#result = segmenter.segment(sentence)
#outfile.write(result.encode('UTF-8'))
#outfile.close()
