# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 20:49:54 2018

@author: yzr
"""

import jieba
import jieba.analyse
import jieba.posseg
import logging
from gensim.models import word2vec


#所有的地名，添加进jieba分词中，防止被切，list_total包括加括号和不加括号的
list_all=[]
with open(r'C:\Users\yzr\Desktop\实验\mydata\list_all.txt',encoding='utf-8') as f:
    list_all=f.readlines()
    list_all_words=[]
    for i in range(0,len(list_all)):
        list_all[i]=list_all[i].split('\t')
    list_all.remove(list_all[0])
    list_place = [[0] for j in range(0,len(list_all))]
    list_place1 = [[0] for j in range(0,len(list_all))]
    
    for t in range(0,len(list_place)):
        list_place[t]=list_all[t][0]
        list_place1[t]=list_place[t]
        
        ind1=list_place[t].find('(')
        if ind1 == -1:
            list_place[t]=list_place[t]
        else:
            list_place[t]=list_place[t][:ind1]
            
list_total=list_place+list_place1

        
#####################################################################
####写入文件有问题
####import codecs
####content = list_total
####f = codecs.open('1224_fenci.txt','w','utf-8')
####f.write(content)
####f.close()
#####################################################################


# 读取评论
with open(r'C:\Users\yzr\Desktop\实验\mydata\comment2.txt','r') as f:
    comment=f.read().split('\n')
    del comment[-1]
print(len(comment))


for i in range(0,len(list_total)):
    jieba.suggest_freq(list_total[i],True)


def stopwordslist(filepath):  
    stopwords = [line.strip() for line in open(filepath, 'r').readlines()]  
    return stopwords  


def seg_sentence(sentence):  
    sentence_seged = jieba.cut(sentence)  
    stopwords = stopwordslist(r'C:\Users\yzr\Desktop\实验\mydata\stopwords.txt')  # 这里加载停用词的路径
    outstr = ''  
    for word in sentence_seged:  
        if word not in stopwords:
            outstr += word
            outstr += " "  
    return outstr                                                                                                                                       

# 前面获得了分词后的结果
user_cut=[]
for user in range(0,len(comment)):
    user_cut.append(seg_sentence(comment[user]))


# 保存分词结果
with open('comment2_segment.txt','w') as f2:
    for i in range(0,len(user_cut)):
        f2.write(user_cut[i])
        f2.write('\n')


# 提取名词
mingci=['n','nr','nr1','nr2','nrj','nrf','ns','nsf','nt','nz','nl','ng']
out=[]
for i in range(0,len(user_cut)):
    a=user_cut[i]
    seg=jieba.posseg.cut(a)
    out_cixing=[]
    for t in seg:
        out_cixing.append((t.word,t.flag))

    s=''
    list_w=[]
    for element in out_cixing:
        if element[1] in mingci:
            list_w.append(element[0])
        a=' '.join(list_w)

    out.append(a)


#保存所有的名词
with open('comment2_segment_mingci.txt', 'wb') as f3:
    for i in range(0,len(out)):
        out[i]=out[i]+'\n'
        result=out[i].encode('utf-8')
        print(result)
        f3.write(result)


#训练word2vec
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#sentences = word2vec.LineSentence('comment2_segment_mingci.txt')
model = word2vec.Word2Vec(out,sg=1,hs=1,min_count=1,window=3,size=100)
# size词向量维度，window词向量上下文最大距离，hs 0 negative samplig， 1 hierarchical softmax，默认0
# min_count需要计算的词向量的最小词频，默认5,sg=1采用skip model


# 保存模型
model.save('word2vec_mingci')
#model.save_word2vec_format('comment_w2v.txt',binary=False)
# model.save_word2vec_format('/data/word2vec.bin'.binary=True)
#model = word2vec.Word2Vec.load_word2vec_format('comment_w2v.bin', binary=True)
#model.save("comment_w2v.txt")


# 加载模型
#from gensim.models import KeyedVectors
#word_vectors = KeyedVectors.load_word2vec_format('vectors.txt', binary=False)  # C text format
#word_vectors = KeyedVectors.load_word2vec_format('vectors.bin', binary=True)  # C binary format


#==============================================================================
# 测试
#读取名词txt
#with open('comment2_segment_mingci.txt',encoding='utf-8') as f4:
#    ceshi=f4.read().split('\n')
#print(len(ceshi))


#req_count = 5
#for key in model.wv.similar_by_word('香格里拉', topn =100):
#    if len(key[0])==3:
#        req_count -= 1
#        print(key[0], key[1])
#        if req_count == 0:
#            break;


# 加载模型
#from gensim.models import Word2Vec
#model=Word2Vec.load('word2vec')
#vector=model.wv['北京']
#print(vector)


# 导出所有的embedding
#keywords=[]

#output = open('keywords_embedding_mingci.txt', 'w')

#for key in model.wv.vocab:
#    keywords.append(key)

# 建立keywords的字典  
#keywords_dic={}
#for word in keywords:
#    vector=model.wv[word]
#    keywords_dic[word]=vector

# 保存keywords和embedding
#for i in keywords:

# 查看keywords中的键和值
#    print(i, place_dic[i])
#    print(place_dic[i])

#    output.write(str(i))
#    output.write('')
#    output.write(str(keywords_dic[i]))
#    output.write('\n')
#    # write_str = str(i) + '' + str(list(dict[i])) + '\n'
#    # output.write(write_str)

#output.close()


# 保存只有keywords的txt
#output1 = open('keywords2_onlywords.txt', 'w')
#
#keywords=[]
#for key in model.wv.vocab:
#    keywords.append(key)
#    
#for i in keywords:
#    output1.write(str(i))
#    output1.write('\n')

#output1.close()
    
