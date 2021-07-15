# %config InlineBackend.figure_format = 'svg'
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams["font.sans-serif"] = 'SimHei'  # 解决中文乱码
plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法正常显示的问题

df = pd.read_csv(r"C:\Users\Administrator\Desktop\python数据分析\订单.csv", encoding='utf-8')
df.set_index('订单编号', inplace=True)
df.head()
s = df['客房类型'].value_counts()
plt.subplot(1, 1, 1)
x = np.array(s.values)
labels = s.index.tolist()
explode = [0.1, 0.05, 0.05, 0.05, 0.05]  # 让第一块离圆心远一点
colors = ["r", "g", "b", "c", "m"]
plt.pie(x, labels=labels, autopct='%3.1f%%', startangle=45, shadow=True, explode=explode, colors=colors)
# 设置标题
plt.title("七月各种房型入住量占比", fontweight="bold")
plt.show()
