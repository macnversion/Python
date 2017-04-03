# -*- coding: utf-8 -*-
# python数据分析与挖掘实战
import pandas as pd
import matplotlib.pyplot as plt


# %% 数据探索
file_path = 'D:\WorkSpace\CodeSpace\data\Python_practice'
catering_scale = file_path + '\chapter3\demo\data\catering_sale.xls'
data = pd.read_excel(catering_scale, index_col=u'日期')
print data.describe()
