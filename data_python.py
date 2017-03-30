# -*- coding: utf-8 -*-
# %%
import numpy as np
from numpy import random
import pandas as pd
from pandas import Series, DataFrame


# %%
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
arr2 = np.array(data2, dtype=np.float32)
arr2.ndim  # 查看arr2的维数
arr2.shape
arr2.dtype
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
