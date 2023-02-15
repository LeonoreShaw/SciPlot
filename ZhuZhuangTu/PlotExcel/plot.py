"""
 笔记本项目：从Excel中读取数据绘制柱状图并保存
 作者：Léonore
 时间：20230126
 常用库：matplotlib.pyplot pandas numpy math scipy
"""

# %% 库的导入

import matplotlib.pyplot as plt
import pandas as pd

# %% 设置字体
config = {
    "font.family": "serif",  # 使用衬线体
    "font.serif": ["SimSun"],  # 全局默认使用衬线宋体
    "font.size": 14,  # 五号，10.5磅
    "axes.unicode_minus": False,
    "mathtext.fontset": "stix",  # 设置 LaTeX 字体，stix 近似于 Times 字体
}
plt.rcParams.update(config)

# %% 从Excel导入数据并加工

name = ['Jacky', 'Rosé', 'Lisa', 'Jisoo']
weight = [123, 89, 92, 80]

# %% 绘制柱状图
plt.bar(name, weight,
        label='体重',  # 图例标签名
        color='purple',  # 颜色
        alpha=0.8,  # 透明度
        width=0.5,  # 条形宽度
        )
# 绘制参数
plt.legend()  # 图例
# plt.title(r'四人体重柱状图$\mu > \alpha$')  # 标题
plt.xlabel(r'姓名（Name）波长($\mathrm{\mu m}$)')  # x轴标签
plt.ylabel(r'体重/斤$\sum_{\pi}^{j=1}\mu x^2\int_2^\pi x \mathrm{d}x$')  # y轴标签

# 调整显示区域
plt.tight_layout()

# 保存图片并显示
# plt.savefig('fig.png', dpi=1000)
plt.show()
