# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 22:07:34 2018

@author: yzr
"""
import re

document=[]
document_new=[]
with open(r'C:\Users\yzr\Desktop\实验\mydata\comment_all.txt',encoding='utf-8') as f:
    document_raw=f.read()
    document=re.split('\s+\d{3}\d+\s+\d\s+',document_raw)
    document[0]=document[0].strip(document[0][0:8])
    
    for i in range(0,len(document)):
        lianjie=document[i].split()
        a=''
        document_new.append(a.join(lianjie))
  
print(len(document_raw))
print(len(document_new))
    

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
    if uchar in ('-',',','，','。','.','>','?','？','！','!'):
            return True

    return False


def is_ustr(in_str):
    out_str=''
    for i in range(len(in_str)):
        if is_uchar(in_str[i]):
            out_str=out_str+in_str[i]
#            print(out_str)
    return out_str


document_new_clean=[]
for i in range(0,len(document_new)):
    if len(document_new[i])!=0:
#        print(document[i][0])
        content=is_ustr(document_new[i])
#        print(content)
        document_new_clean.append(content)
        
print(len(document_new_clean))


f1=open('comment2.txt','w') #新建输出文件
for i in range(0,len(document_new_clean)):
    print(document_new_clean[i])
    print(i)
    f1.write(document_new_clean[i])
    f1.write('\n')
f1.close()