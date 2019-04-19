# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 16:35:07 2019

@author: yzr
"""

import numpy as np
import re
from gensim.models import Word2Vec


#model = word2vec.Word2Vec.load('word2vec_mingci')
#model = word2vec.KeyedVectors.load_word2vec_format('model2/word2vec_sohucorpus.model.bin', binary=True)


#y6 = model.vector_size #词向量维度
#print('词向量维度:', y6) #python3
#print(u"词向量维度:", y6) #python2 正常显示中文，去掉括号
#print('词向量维度:', y6) 


# 景点可视化
with open('list3_jingdian_embedding.txt','r') as f:
    jingdian=f.read().split()


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


#调用embedding
#加载模型
model=Word2Vec.load('word2vec')

#导出所有的embedding

jingdian_embedding=[]
for i in list_3: 
    if i in model.wv.vocab:
        vector=model.wv[i]
        jingdian_embedding.append([i,vector])
    

## 模型可视化
## 使用t-SNE可视化学习的嵌入。t-SNE是一种数据可视化工具，可将数据的维度降至2或3维，从而可以轻松进行绘制。
## 由于t-SNE算法的空间复杂度是二次的，因此在本教程中，我们将仅查看模型的一部分。
## 我们使用下面的代码从我们的词汇中选择10,000个单词
#count = len(model.wv.vocab)
count=383
word_vectors_matrix = np.ndarray(shape=(count, 100), dtype='float32')
word_list = []
i = 0
for word in jingdian_embedding:
	word_vectors_matrix[i] = word[1]
	word_list.append(word[0])
	i = i+1
	if i == count:
		break
print("word_vectors_matrix shape is: ", word_vectors_matrix.shape)

# 由于模型是一个300维向量，利用Scikit-Learn 中的降维算法t-SNE
# 初始化模型并将我们的单词向量压缩到二维空间
import sklearn.manifold as ts
tsne = ts.TSNE(n_components=2, random_state=0)
word_vectors_matrix_2d = tsne.fit_transform(word_vectors_matrix)
print("word_vectors_matrix_2d shape is: ", word_vectors_matrix_2d.shape)


# 数据框，其中包含所选单词和每个单词的x和y坐标
import pandas as pd
points = pd.DataFrame(
	[(word, coords[0], coords[1]) for word, coords in [(word, word_vectors_matrix_2d[word_list.index(word)])
													   for word in word_list] ], columns=["word", "x", "y"])
print("Points DataFrame built")
print(points.head(10))


#DataFrame来绘制我们的单词向量
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import mpl


##方法一
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体：解决plot不能显示中文问题,否则会显示成方块
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


## #方法二
#myfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/simsunb.ttf')
#mpl.rcParams['axes.unicode_minus'] = False
#plt.title(u'标题', fontproperties=myfont)

#sns.set_context('poster') #四种预设，按相对尺寸的顺序(线条越来越粗)，分别是paper，notebook, talk, and poster
#points.plot.scatter("x", "y", s=10, figsize=(20, 12))
#plt.show()


## 放大到一些区域，以便看到单词的相似性。我们创建一个函数，
## 创建x和y坐标的边界框，并只绘制该边界框之间的单词。
def plot_region(x_bounds, y_bounds):
	slice = points[
		(x_bounds[0] <= points.x) &
		(points.x <= x_bounds[1]) &
		(y_bounds[0] <= points.y) &
		(points.y <= y_bounds[1])
		]

	ax = slice.plot.scatter("x", "y", s=10, figsize=(20, 12))
	for  i, point in slice.iterrows():
		ax.text(point.x + 0.05, point.y + 0.05, point.word, fontsize=11) # text可以将文本绘制在图表指定坐标(x,y)
plot_region(x_bounds=(-200, 200), y_bounds=(-200, 200))


plt.savefig('jingdian.jpg')
plt.show()