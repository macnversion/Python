# -*- coding: utf-8 -*-
# %%
import numpy as np
from numpy import random


# %%
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
data2 = [[1,2,3,4], [5,6,7,8]]
arr2 = np.array(data2)
arr2 = np.array(data2, dtype=np.float32)
arr2.ndim # 查看arr2的维数
arr2.shape
arr2.dtype
np.zeros(10)
np.arange(15)
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

names = np.array(['bob', 'joe', 'will', 'bob', 'will', 'joe', 'joe'])
data = np.random.randn(7,4)
data[names=='bob']
arr = np.arange(32).reshape(4,8).reshape(8,4)