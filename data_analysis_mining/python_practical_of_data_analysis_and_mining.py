# -*- coding: utf-8 -*-
#  python数据分析与挖掘实战

# %%
from sklearn import datasets
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import platform
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
# %%
data_path = r'/Users/machuan/CodeSpace/Code.Data/python/'

# %% 数据探索- chapter03
file_path = data_path + r'Python数据分析与挖掘实战/chapter3/demo/data/'
# 异常分析和离散度分析
catering_sale = file_path + 'catering_sale.xls'
data = pd.read_excel(catering_sale, index_col=u'日期')

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure()
p = data.boxplot()
# x = p['fliers'][0].get_xdata() # 'flies'即为异常值的标签 # fix me
# y = p['fliers'][0].get_ydata() # fix me
# y.sort


data = data[(data[u'销量'] > 400) & (data[u'销量'] < 5000)]  # 过滤异常数据
statistics = data.describe()  # 保留基本统计量

statistics.loc['range'] = statistics.loc['max'] - statistics.loc['min']
statistics.loc['var'] = statistics.loc['std']/statistics.loc['mean']
statistics.loc['dis'] = statistics.loc['75%'] - statistics.loc['25%']

#  贡献度分析
dish_profit = pd.read_excel(file_path + 'catering_dish_profit.xls',
                            index_col=u'菜品名')
data = dish_profit[u'盈利'].copy()
data.sort(ascending=False)

plt.figure()
data.plot(kind='bar')
plt.ylabel(u'盈利（元）')
p = 1.0*data.cumsum()/data.sum()
p.plot(color='red', secondary_y=True, style='-o', linewidth=2)


# 相关度分析
catering_sale_all = pd.read_excel(file_path + 'catering_sale_all.xls',
                                  index_col=u'日期')

# %% 数据预处理
file_path = data_path + r'Python数据分析与挖掘实战/chapter4/demo/data/'

# 拉格朗日插值
catering_sale = pd.read_excel(file_path + 'catering_sale.xls',
                              index_col=u'日期')
catering_sale[u'销量'][(catering_sale[u'销量']<400)|
                     (catering_sale[u'销量']>5000)] = None


# 自定义插值函数
# s为列向量，n为被插值的位置，k为取前后的数据的个数
def ployinterp_columns(s, n, k=5):
    y = s[list(range(n-k, n) + list(n+1, n+k+1))]
    y = y[y.notnull()]
    return lagrange(y.index, list(y))[n]


for i in catering_sale.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            data[i][j] = ployinterp_columns(data[i], j)

# 连续属性离散化
discretization_data = pd.read_excel(file_path + 'discretization_data.xls')
data = discretization_data.[u'肝气郁结证型系数'].copy()
