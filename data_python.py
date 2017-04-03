# -*- coding: utf-8 -*-
# %%
import numpy as np
from numpy import random
import pandas as pd
from pandas import DataFrame, Series
from datetime import datetime


# %%
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
arr2 = np.array(data2, dtype=np.float32)
print arr2.ndim  # 查看arr2的维数
print arr2.shape
print arr2.dtype
np.zeros(10)
np.arange(15)
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

names = np.array(['bob', 'joe', 'will', 'bob', 'will', 'joe', 'joe'])
data = np.random.randn(7, 4)
data[names == 'bob']
arr = np.arange(32).reshape(4, 8).reshape(8, 4)
x = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
y = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
con = np.array([True, False, True, False, True])
result1 = [(x1 if c else y1) for x1, y1, c in zip(x, y, con)]
result2 = np.where(con, x, y)

frame = DataFrame(np.arange(16).reshape(4, 4),
                  index=['a', 'b', 'c', 'd'],
                  columns=['Ohio', 'Texas', 'Cali', 'New York'])
f = lambda x: x.max() - x.min()
frame.apply(f)
frame.apply(f, axis=1)
frame.sort_index()
frame.sort_index(axis=1)
# 根据多列的名称进行排序
frame.sort_index(by=['Ohio', 'Texas'])
frame2 = frame.set_index(['Ohio', 'Texas'], drop=False)

# 数据的合并
df1 = DataFrame({'lkey':['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1':range(7)})
df2 = DataFrame({'rkey':['a', 'b', 'd'],
                 'data2':range(3)})
pd.merge(df1, df2, left_on='lkey', right_on='rkey', how='right')

left = DataFrame({'key1':['foo', 'foo', 'bar'],
                  'key2':['one', 'two', 'one'],
                  'lval':[1,2,3]})
right = DataFrame({'key1':['foo', 'foo', 'bar', 'bar'],
                   'key2':['one', 'two', 'one', 'two'],
                   'rval':[4,5,6,7]})
left1 = DataFrame({'key':['a', 'b', 'a', 'a', 'b', 'c'],
                   'value':range(6)})
right1 = DataFrame({'group_val':[3.5, 7]},
                    index=['a', 'b'])
pd.merge(left, right, on=['key1', 'key2'], how='outer')
pd.merge(left, right, on='key1', suffixes=('_left', '_right'))
pd.merge(left1, right1, left_on='key', right_index=True,
         how='outer')


s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])
s4 = pd.concat([s1*5, s3])
pd.concat([s1, s2, s3])
pd.concat([s1, s2, s3], axis=1)
pd.concat([s1, s4], axis=1, join='inner')
result1 = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])
result2 = pd.concat([s1, s1, s3], axis=1,
                    keys=['one', 'two', 'three'])

data = DataFrame(np.arange(6).reshape(2,3),
                 index=pd.Index(['ohio', 'colorado'], name='state'),
                 columns=pd.Index(['one', 'two', 'three'],
                                  name='number'))
# 离散化和面元划分
ages = [15, 17, 23, 25, 29, 31, 33, 28, 34, 40, 50]
bins = [18, 25, 35, 40, 100]
cats = pd.cut(ages, bins)
cats.codes
