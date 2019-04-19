# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 20:52:49 2018

@author: yzr
"""

import jieba
import jieba.analyse
import logging
from gensim.models import word2vec


with open(r'C:\Users\yzr\Desktop\实验\mydata\list_all.txt',encoding='utf-8') as f:
    list_all=f.readlines()
    list_all_words=[]
    for i in range(0,len(list_all)):
        list_all[i]=list_all[i].split()
    list_all.remove(list_all[0])
    list_place = [[0] for j in range(0,len(list_all))]
    list_place1 = [[0] for j in range(0,len(list_all))]
    
    for t in range(0,len(list_place)):
        list_place[t]=list_all[t][0]
        list_place1[t]=list_all[t][0]

        ind1=list_place[t].find('(')
        if ind1 == -1:
            list_place[t]=list_place[t]
        else:
            list_place[t]=list_place[t][:ind1]

list_total=list_place+list_place1


for i in range(0,len(list_total)):
    jieba.suggest_freq(list_total[i],True)


#with open('comment1.txt','rb') as f:
#    document=f.read().split()
#    for line in document:
#        seg=jieba.cut(line,cut_all=False)
#        result=' '.join(seg)
#        m=list(result)
#        with open('comment1_segment.txt', 'a+') as f:
#            for word in m:
#                f.write(word)


with open('comment1.txt','rb') as f:
    document = f.read()
    
    #document_decode = document.decode('GBK')
    
    document_cut = jieba.cut(document)
    #print  ' '.join(jieba_cut)  //如果打印结果，则分词效果消失，后面的result无法显示
    result = ' '.join(document_cut)
    result = result.encode('utf-8')
    with open('comment1_segment.txt', 'wb') as f2:
        f2.write(result)
f.close()
f2.close()


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.LineSentence('comment1_segment.txt') 
model = word2vec.Word2Vec(sentences, hs=1,min_count=1,window=3,size=100)
##size词向量维度，window词向量上下文最大距离，hs 0 negative samplig， 1 hierarchical softmax，默认0
##min_count需要计算的词向量的最小词频，默认5


# 保存模型
##model.save('word2vec')
##model.save_word2vec_format('comment_w2v.txt',binary=False)
## model.save_word2vec_format('/data/word2vec.bin'.binary=True)
##model = word2vec.Word2Vec.load_word2vec_format('comment_w2v.bin', binary=True)
##model.save("comment_w2v.txt")
##
##from gensim.models import KeyedVectors
##word_vectors = KeyedVectors.load_word2vec_format('vectors.txt', binary=False)  # C text format
##word_vectors = KeyedVectors.load_word2vec_format('vectors.bin', binary=True)  # C binary format


#==============================================================================
# 测试
req_count = 5
for key in model.wv.similar_by_word('香山', topn =100):
    if len(key[0])==3:
        req_count -= 1
        print(key[0], key[1])
        if req_count == 0:
            break;

#from gensim.models import Word2Vec
#model=Word2Vec.load('word2vec')

#vector=model.wv['北京']
#print(vector)
