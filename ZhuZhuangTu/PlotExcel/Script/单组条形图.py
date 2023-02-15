import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import openpyxl

config = {
    "font.family": "serif",  # 使用衬线体
    "font.serif": ["SimSun"],  # 全局默认使用衬线宋体 "SimHei"黑体
    "font.weight": 'normal',  # bold粗体,bolder更粗,lighter更细.400等同于normal700等同于bold
    "font.size": 14,  # 五号，10.5磅 .'medium',#or large,small
    "axes.unicode_minus": False,
    "mathtext.fontset": "stix",  # 设置 LaTeX 字体，stix 近似于 Times 字体
}
plt.rcParams.update(config)

# 读取数据
数据 = pd.read_excel('F:\PycharmProjects\科研绘图\ZhuzhuangTu\PlotExcel\数据.xlsx')
# 显示数据
print(数据)  # pandas.series
# series转换成列表
患者 = 数据.患者.tolist()
收缩压 = 数据.收缩压.tolist()
舒张压 = 数据.舒张压.tolist()

# plt.subplots()是一个函数，返回一个包含figure和axes对象的元组。因此，使用 fig,ax = plt.subplots()将元组分解为fig和ax两个变量。
fig, ax = plt.subplots()
bar_labels = ['green', 'blue', 'red', 'orange']
bar_colors = ['tab:green', 'tab:blue', 'tab:red', 'tab:orange']
bar_widths = [0.2, 0.3, 0.5, 0.6]
ax.bar(患者[0:4]
       , 舒张压[0:4]
       , label=bar_labels
       , color=bar_colors
       , alpha=0.8
       , width=bar_widths
       )
ax.set_title(r'Fruit四人体重柱状图$\mu > \alpha$'
             , fontsize=18
             , weight='bold'
             )
ax.set_xlabel(r'姓名（Name）波长($\mathrm{\mu m}$)'
              , fontsize=12
              , weight='bold'
              )
ax.set_ylabel(r'体重/斤$\sum_{\pi}^{j=1}\mu x^2\int_2^\pi x \mathrm{d}x$'
              , fontsize=12
              , weight='bold'
              )
ax.legend(title='Fruit color'
          , loc="upper center"
          )

# 调整显示区域
fig.tight_layout()
# 保存图片并显示
# plt.savefig('../图片/单组示例.pdf', dpi=1000)
plt.show()
