# -*- coding: utf-8 -*-
#  python数据分析与挖掘实战

# %%
import os
import platform
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR
from sklearn import datasets
# %%
if 'Windows' in platform.platform():
    data_path = r'D:/WorkSpace/CodeSpace/Code.Data/Python/'
else:
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
            data[i][j] = ployinterp_columns(data[i], j)  # fix me

# 连续属性离散化
# 数据规范化
discretization_data = pd.read_excel(file_path + 'discretization_data.xls')
data = discretization_data[u'肝气郁结证型系数'].copy()
k = 4
d1 = pd.cut(data, k, labels=range(k))

# 等频率离散化
w = [1.0*i/k for i in range(k+1)]
w = data.describe(percentiles=w)[4:4+k+1]
w[0] = w[0]*(1-1e-10)
d2 = pd.cut(data, w, labels=range(k))

kmodel = KMeans(n_clusters=k, n_jobs=4)
kmodel.fit(data.reshape(len(data), 1))
c = DataFrame(kmodel.cluster_centers_).sort(0)
w = pd.rolling_mean(c, 2).iloc[1:]
w = [0] + list(w[0]) + [data.max()]
d3 = pd.cut(data, w, labels=range(k))


def cluster_plot(d, k):
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    for j in range(0, k):
        plt.plot(data[d==j], [j for i in d[d==j]], 'o')

    plt.ylim(-0.5, k-0.5)
    return plt

cluster_plot(d1, k).show()
cluster_plot(d2, k).show()
cluster_plot(d3, k).show()

# 主成分分析
principal_component = pd.read_excel(file_path + 'principal_component.xls',
                                    header=None)
pca = PCA()
pca.fit(principal_component)
pca.components_
pca.explained_variance_ratio_

pca = PCA(3)
pca.fit(principal_component)
low_d = pca.transform(principal_component)


# %% 挖掘建模
file_path = data_path + r'Python数据分析与挖掘实战/chapter5/demo/data/'

# 逻辑回归
bankloan = pd.read_excel(file_path + 'bankloan.xls')
x = bankloan.iloc[:, :8].as_matrix()
y = bankloan.iloc[:, 8].as_matrix()

rlr = RLR()
rlr.fit(x, y)
rlr.get_support()
