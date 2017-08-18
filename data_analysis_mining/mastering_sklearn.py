# -*- coding: utf-8 -*-

# %%
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from sklearn.linear_model import LinearRegression
# %% 线性回归
# 一元线性回归
def runplt():
    plt.figure()
    plt.title(u'披萨价格与直径数据')
    plt.xlabel(u'直径（英寸）')
    plt.ylabel(u'价格（美元）')
    plt.axis([0, 25, 0, 25])
    plt.grid(True)
    return plt

plt = runplt()
x = [[6], [8], [10], [14], [18]]
y = [[7], [9], [13], [17.5], [18]]
plt.plot(x, y, 'k.')
plt.show()