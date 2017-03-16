# -*- coding: utf-8 -*-
import jieba  
import jieba.posseg  
print "Full Mode:","/".join(jieba.cut('始游泳'))  
print "Full Mode:","/".join(jieba.cut('过郭美美'))  
s=["我勒个去","费打电话","响全世界","线情人"]  
for i in s:  
    pos=[]  
    seg=jieba.posseg.cut(i)  
    for j in seg:  
        print j.word,'/',j.flag,'#',  
        pos.append([j.word,j.flag])  
    print    
#----------------------------------  
string="当我输给青雉的时候就在想，在以后的航海中再遇到像他那么强的对手的时候"  
seg=jieba.posseg.cut(string)  
pos=[]  
for i in seg:  
    pos.append([i.word,i.flag])  
for i in pos:  
    print i[0],'/',i[1],"#", 