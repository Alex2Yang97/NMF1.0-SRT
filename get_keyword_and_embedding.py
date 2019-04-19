# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 17:04:11 2019

@author: yzr
"""
import re


with open('list_all.txt',encoding='utf-8') as f:
    list_jingdian=f.readlines()

    
    list_all_words=[]
    for i in range(0,len(list_jingdian)):
        list_jingdian[i]=list_jingdian[i].split()
    list_jingdian.remove(list_jingdian[0])
    
    list_1=[]
#    list_2=[]
    list_3=[]
    list_4=[]
    
    for i in range(0,len(list_jingdian)):
        if list_jingdian[i][1]=='1':
            list_1.append(list_jingdian[i][0])
#        if list_jingdian[i][1]=='2':
#            list_2.append(list_jingdian[i][0])
        if list_jingdian[i][1]=='3':
            list_3.append(list_jingdian[i][0])
        if list_jingdian[i][1]=='4':
            list_4.append(list_jingdian[i][0])

print('list_1 : ',len(list_1))
print('list_3 : ',len(list_3))
print('list_4 : ',len(list_4))


def translate(str):
    p2 = re.compile(u'[^\u4e00-\u9fa5]')  
    zh = " ".join(p2.split(str)).strip()
    zh = " ".join(zh.split())
    return zh


#f1=open('list_1.txt','w') #新建输出文件
#for i in range(0,len(list_1)):
##    list_1[i].encode('utf-8')
#    list_w=translate(list_1[i])
#    f1.write(list_w)
#    f1.write('\n')
#f1.close()


#f1=open('list_3.txt','w') #新建输出文件
#for i in range(0,len(list_3)):
#    f1.write(list_3[i])
#    f1.write('\n')
#f1.close()


# 调用embedding
# 加载模型
from gensim.models import Word2Vec
model=Word2Vec.load('word2vec')


#导出所有的embedding
jingdian_embedding=[]
for i in list_3: 
    if i in model.wv.vocab:
        vector=model.wv[i]
        jingdian_embedding.append([i,vector])
    

output = open('list3_jingdian_embedding.txt', 'w')


# 保存keywords和embedding
for jingdian in jingdian_embedding:

    # 查看keywords中的键和值
    # print(jingdian[0])
    # print(jingdian[1])

    output.write(jingdian[0]+',')
    output.write('')
    a=str(list(jingdian[1]))
    a=a.strip('[').strip(']')
    print(a)
    output.write(a)
    output.write('\n')
    # write_str = str(i) + '' + str(list(dict[i])) + '\n'
    # output.write(write_str)
output.close()


# 读取保存了的 keyword 和 embedding
#with open('list3_jingdian.txt','w') as f1:
#    for jingdian in jingdian_embedding:
#        f1.write(jingdian[0])
#        f1.write('\n')


    
    