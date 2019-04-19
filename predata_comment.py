# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 18:11:32 2018

@author: yzr
"""


document=[]
with open(r'C:\Users\yzr\Desktop\实验\mydata\comment_all.txt',encoding='utf-8') as f:
    document=f.read().split('\n')
    
print(len(document))

for i in range(0,len(document)):
    t_ind=document[i].find('\t') 
    while(t_ind!=-1):
        document[i]=document[i][t_ind+1:]
        t_ind=document[i].find('\t')
    document[i]=document[i].split()
    
print(len(document))

def is_uchar(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
            return True
    """判断一个unicode是否是数字"""
    if uchar >= u'\u0030' and uchar<=u'\u0039':
            return True        
    """判断一个unicode是否是英文字母"""
    if (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a'):
            return True

    return False

def is_ustr(in_str):
    out_str=''
    for i in range(len(in_str)):
        if is_uchar(in_str[i]):
            out_str=out_str+in_str[i]
#            print(out_str)
    return out_str


document1=[]
for i in range(0,len(document)):
    if len(document[i])!=0:
#        print(document[i][0])
        content=is_ustr(document[i][0])
#        print(content)
        document1.append(content)
        
print(len(document1))

    
f1=open('comment1.txt','w') #新建输出文件
for i in range(0,len(document1)):
    print(document1[i])
    f1.write(document1[i])
    f1.write('\n')
f1.close()