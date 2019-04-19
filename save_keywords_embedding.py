# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 16:15:16 2018

@author: yzr
"""

from gensim.models import Word2Vec

model=Word2Vec.load('word2vec')
vector=model.wv['北京']
print(vector)

#找交集，找出交集词语的embedding
with open(r'C:\Users\yzr\Desktop\实验\mydata\fenci1.txt','r') as f:
    place=f.read().split()

print(place[0:10])

with open(r'C:\Users\yzr\Desktop\实验\mydata\comment1_segment.txt',encoding='utf-8') as f:
    comment=f.read().split()

print(comment[0:10])

intersection = list(set(place).intersection(set(comment)))
print(len(intersection))
print(intersection[0:10])

#place_dic={}
#for com in intersection:
#    vector=model.wv[com]
#    place_dic[com]=vector
    
#print(place_dic)



#output = open('keywords_embedding_fenci1_jingzhunmoshi.txt', 'w')
#for i in place_dic:
##    print(i, place_dic[i])
##    print(place_dic[i])
# 
#    output.write(str(i))
#    output.write('')
#    output.write(str(place_dic[i]))
#    output.write('\n')
#    # write_str = str(i) + '' + str(list(dict[i])) + '\n'
#    # output.write(write_str)
#
#output.close()

output = open('keywords_onlywords1.txt', 'w')
output.write(str(intersection))
#    print(i, place_dic[i])
#    print(place_dic[i])

    # write_str = str(i) + '' + str(list(dict[i])) + '\n'

output.close()
