# -*- coding: utf-8 -*-
# %%
import numpy as np
from numpy import random
import pandas as pd
from pandas import DataFrame, Series
from datetime import datetime
import json
from collections import defaultdict
from collections import Counter


# %% function
def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x]+=1
        else:
            counts[x]=1
    return counts


def get_counts2(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts


def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

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

# %% usagov数据
data_path = 'D:\WorkSpace\CodeSpace\data\python_for_data_analysis'
path = data_path + '\ch02\usagov_bitly_data2012-03-16-1331923249.txt'
open(path).readline()

records = [json.loads(line) for line in open(path)]

time_zones = [rec['tz'] for rec in records if 'tz' in rec]
top_counts(get_counts(time_zones))
counts = Counter(time_zones)
counts.most_common(10)

frame = DataFrame(records)
tz_counts = frame['tz'].value_counts()
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == '']='Unknown'
tz_counts = clean_tz.value_counts()
tz_counts[:10].plot(kind='barh', rot=20)

results = Series([xx.split()[0] for xx in frame.a.dropna()])
results.value_counts()[:10]
cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'),
                            'windodws', 'Not Windows')
by_tz_os = cframe.groupby(['tz', operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
indexer = agg_counts.sum(1).argsort()
count_subset = agg_counts.take(indexer)[-10:]

# %% movielens 1M数据集
data_path = 'D:\WorkSpace\CodeSpace\data\python_for_data_analysis'
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
mnames = ['movie_id', 'title', 'genres']
users = pd.read_table(data_path+'\ch02\movielens\users.dat',
                      sep='::', header=None, names=unames,
                      engine='python')
ratings = pd.read_table(data_path+'\ch02\movielens\\ratings.dat',
                        sep='::', header=None, names=rnames,
                        engine='python')
movies = pd.read_table(data_path+'\ch02\movielens\movies.dat',
                       sep='::', header=None, names=mnames,
                       engine='python')
data = pd.merge(pd.merge(ratings, users), movies)
# %%
mean_rating = data.pivot_table('rating', index='title', columns='gender',
                             aggfunc='mean')
rating_by_title = data.groupby('title').size()
active_titles = rating_by_title.index[rating_by_title>250]
mean_rating = mean_rating.ix[active_titles]
top_female_movies = mean_rating.sort_values(by='F', ascending=False)
mean_rating['diff'] = mean_rating['F'] - mean_rating['M']
sort_by_diff = mean_rating.sort_values(by='diff', ascending=False)
rating_std_by_title = data.groupby('title')['rating'].std()

# %% 美国出生的婴儿的姓名
data_path = 'D:\WorkSpace\CodeSpace\data\python_for_data_analysis'
names1880 = pd.read_csv(data_path+'\ch02\\names\yob1880.txt',
                        names=['name', 'sex', 'births'])
names1880.groupby('sex').births.sum()
years = range(1880, 2011)
pieces = []
columns = ['name', 'sex', 'births']
for year in  years:
    path = data_path + ('\ch02\\names\yob%d.txt' % year)
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)
names = pd.concat(pieces, ignore_index = True)
# %%
total_births = names.pivot_table('births', index='year', columns='sex')