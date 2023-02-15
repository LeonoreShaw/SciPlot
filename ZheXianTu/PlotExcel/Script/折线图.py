import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib.font_manager import FontProperties
from scipy.interpolate import interp1d

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

values = [2.2, 2.3, 2.5, 3, 3.8, 4, 5, 5.1, 5.2, 5.5, 6, 7, 7.2, 7.5, 7.6, 7.75, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
          18, 19, 20, 21, 22, 23, 24, 25]
x = np.linspace(2.2, 25, 5000)
data1 = [0.31, 0.32, 0.28, 0.35, 0.37, 0.34, 0.76, 0.8, 0.82, 0.88, 0.95, 0.97, 0.975, 0.984, 0.992, 0.995, 0.999, 1.0,
         0.92, 0.73, 0.74, 0.7, 0.67, 0.61, 0.62, 0.7, 0.78, 0.79, 0.77, 0.72, 0.7, 0.65, 0.63, 0.62]
x1 = np.linspace(2.2, 25, 5000)
y1 = interp1d(values, data1, 'cubic')
yy1 = y1(x1)
data2 = [0.32, 0.34, 0.29, 0.36, 0.38, 0.385, 0.78, 0.82, 0.84, 0.89, 0.95, 0.973, 0.975, 0.984, 0.992, 0.995, 0.999,
         1.0, 0.92, 0.83, 0.78, 0.72, 0.69, 0.62, 0.6, 0.7, 0.77, 0.79, 0.77, 0.75, 0.73, 0.68, 0.65, 0.62]
x2 = np.linspace(2.2, 25, 5000)
y2 = interp1d(values, data2, 'cubic')
yy2 = y2(x2)
data3 = [0.35, 0.36, 0.3, 0.37, 0.39, 0.39, 0.78, 0.835, 0.85, 0.91, 0.95, 0.97, 0.98, 0.984, 0.992, 0.995, 0.999, 1.0,
         0.92, 0.88, 0.8, 0.77, 0.7, 0.66, 0.62, 0.7, 0.77, 0.79, 0.77, 0.765, 0.75, 0.67, 0.66, 0.62]
x3 = np.linspace(2.2, 25, 5000)
y3 = interp1d(values, data3, 'cubic')
yy3 = y3(x3)
data4 = [0.4, 0.36, 0.30, 0.38, 0.39, 0.40, 0.79, 0.84, 0.87, 0.918, 0.95, 0.98, 0.985, 0.988, 0.992, 0.995, 0.999, 1.0,
         0.92, 0.9, 0.84, 0.8, 0.76, 0.68, 0.62, 0.7, 0.76, 0.79, 0.78, 0.75, 0.73, 0.65, 0.65, 0.62]
x4 = np.linspace(2.2, 25, 5000)
y4 = interp1d(values, data4, 'cubic')
yy4 = y4(x4)

data = [yy1, yy2, yy3, yy4]
data = np.transpose(data)
wide_df = pd.DataFrame(data, x, ["200$^{\circ}$C", "400$^{\circ}$C", "600$^{\circ}$C", "800$^{\circ}$C"])
f = sns.lineplot(data=wide_df, palette='gist_rainbow')  # gist_rainbow
f.set_xlabel(r'波长($\mathrm{\mu m}$)')
f.set_ylabel(r"-发射率-")
f.set_ylim(0, 1.1)
saveF = f.get_figure()
# saveF.savefig('../图片/fig.pdf', dpi=1200)
saveF.show()
