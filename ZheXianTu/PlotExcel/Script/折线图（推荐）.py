import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.interpolate import interp1d
import openpyxl

# %% 设置字体

config = {
    "font.family": "serif",  # 使用衬线体
    "font.serif": ["SimSun"],  # 全局默认使用衬线宋体
    "font.size": 14,  # 五号，10.5磅
    "axes.unicode_minus": False,
    "mathtext.fontset": "stix",  # 设置 LaTeX 字体，stix 近似于 Times 字体
}
plt.rcParams.update(config)

# %%

fig, ax = plt.subplots()  # 创建图实例
x = np.linspace(0, 20, 5)  # 创建x的取值范围
y1 = x
y2 = x**2
y3 = x**3

数据 = pd.read_excel("data.xlsx")

# series转换成列表
城市 = 数据.城市.tolist()
人 = 数据.人.tolist()
钱 = 数据.钱.tolist()

ax.plot(
    城市,
    人,
    linestyle="dashdot",  # -实线(solid), --短线(dashed), -.短点相间线(dashdot), :虚点线(dotted)
    linewidth=2,  # 线宽
    marker="*"  # 数据点形状.点,像素点o圆v向下三角形^向上三角形<向左三角形>向右三角形
    # 1向下T形2向上T形3向左T形4向右T形
    # s正方形p五边形*星型h六边形1H六边形2
    # +十字形x叉D大菱形d小菱形|竖线_横线
    ,
    markeredgecolor="blue",  # 边框颜色
    markeredgewidth=2,  # 边框粗细
    markerfacecolor="#048210",  # 填充色
    markersize=8,  # 标记大小
    alpha=0.2,  # 透明度
    label="一次",
    color="red",
)  # 作y1 = x 图，并标记此线名为linear
ax.plot(
    城市,
    钱,
    linestyle="dotted",  # -实线(solid), --短线(dashed), -.短点相间线(dashdot), :虚点线(dotted)
    linewidth=4,  # 线宽
    marker="x",  # 数据点形状
    markeredgecolor="blue",  # 边框颜色
    markeredgewidth=2,  # 边框粗细
    markerfacecolor="#048210",  # 填充色
    markersize=8,  # 标记大小
    alpha=0.8,  # 透明度
    label="quadratic",
    color="#008FF0",
)  # 作y2 = x^2 图，并标记此线名为quadratic
list2 = np.sum([钱, 人], axis=0).tolist()
ax.plot(
    城市,
    list2,
    linestyle="dashed",  # -实线(solid), --短线(dashed), -.短点相间线(dashdot), :虚点线(dotted)
    linewidth=3,  # 线宽
    marker="H",  # 数据点形状
    markeredgecolor="#8F8210",  # 边框颜色
    markeredgewidth=3,  # 边框粗细
    markerfacecolor="#0F8210",  # 填充色
    markersize=10,  # 标记大小
    alpha=0.5,  # 透明度
    label="cubic",
    color="purple",
)  # 作y3 = x^3 图，并标记此线名为cubic

ax.set_title(
    r"$\sum\int\alpha$Simple Plot好的", fontsize=20, weight="bold"
)  # 设置图名为Simple Plot
ax.set_xlabel(
    "x label波长($\mathrm {\mu m}$)", fontsize=16, weight="bold"
)  # 设置x轴名称 x label
ax.set_ylabel(r"这是y label的$\mu m$", fontsize=16, weight="bold")  # 设置y轴名称 y label
ax.legend(title="Fruit color", loc="upper left")
# 在折线图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
for a, b in zip(x, y1):
    ax.text(a, b, b, ha="center", va="bottom", fontsize=10, rotation=0)
# for a, b in zip(x, y2):
#     ax.text(a, b, str(b), ha='center', va='bottom', fontsize=20, rotation=0)
for a, b in zip(x, y3):
    ax.text(a, b, (a, b), ha="right", va="top", fontsize=20, rotation=0)

# 调整显示区域
plt.tight_layout()

# 保存图片并显示
# plt.savefig('../图片/示例.pdf', dpi=1000)
plt.show()
