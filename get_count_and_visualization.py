# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 08:50:18 2018

@author: yzr
"""


from collections import Counter

# 统计评论所有的词频
with open('comment2_segment.txt','r')as f:
    comment=f.read().split()
print(len(comment))


cnt=Counter()
for word in comment:
    cnt[word]+=1   


comment_cipin=[]
for t in cnt.most_common():
    comment_cipin.append(list(t))
#    print(comment_cipin)

   
with open('cipin_all.txt','w') as f1:
    for i in comment_cipin:
        f1.write(i[0])
        f1.write('\t')
        f1.write(str(i[1]))
        f1.write('\n')

     
# 只统计名词词频
with open('comment2_segment_mingci.txt',encoding='utf-8') as f3:
    mingci=f3.read().split()
print(len(mingci))


cnt_mingci=Counter()
for word in mingci:
    cnt_mingci[word]+=1

    
mingci_cipin=[]
for t in cnt_mingci.most_common():
    mingci_cipin.append(list(t))
    print(comment_cipin)


# 删除一个字的名词
mingci_cipin_ci=[]
for ci in mingci_cipin:
    if len(ci[0]) !=1:
#        print(ci[0])
        mingci_cipin_ci.append(ci)
    
with open('cipin_mingci_ci.txt','w') as f4:
    for i in mingci_cipin_ci:
        f4.write(i[0])
        f4.write('\t')
        f4.write(str(i[1]))
        f4.write('\n')

# 绘图
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif']=['FangSong']
mpl.rcParams['axes.unicode_minus']=False

label = list(map(lambda x: x[0], cnt_mingci.most_common()[:100]))
value = list(map(lambda y: y[1], cnt_mingci.most_common()[:100]))

plt.xticks(fontsize=3)
plt.xticks(rotation=90)

plt.bar(range(len(value)), value, tick_label=label)

plt.savefig('ciping_mingci100.png', dpi=400, bbox_inches='tight')
plt.show()

