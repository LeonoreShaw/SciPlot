"""
 笔记本项目：从Excel中读取数据
 作者：Léonore
 时间：20230126
 常用库：matplotlib.pyplot pandas numpy math scipy
"""

# %% 库的导入


import pandas as pd

# %% 从Excel导入数据并加工

# 读取Excel文件数据为Dataframe
数据 = pd.read_excel('F:\PycharmProjects\科研绘图\ZhuzhuangTu\PlotExcel\数据.xlsx')
print(数据)
print("*********************************************")

收缩压 = 数据.收缩压
舒张压 = 数据.舒张压
print(收缩压)
print(舒张压)
