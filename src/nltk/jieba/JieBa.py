# -*- coding: utf-8 -*-

import jieba.analyse
import jieba
import jieba.posseg as pseg
import time

string=u'当我输给青雉的时候就在想，在以后的航海中再遇到像他那么强的对手的时候'

words = pseg.cut(string) #进行分词

result=''  #记录最终结果的变量
for w in words:
    result+= w.word.encode('utf8')+'|'+w.flag.encode('utf8')#加词性标注

f=open('t_with_POS_tag.txt','w')  #将结果保存到另一个文档中

f.write(result)
f.close()
t2=time.time()

print result
