# %config InlineBackend.figure_format = 'svg'
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams["font.sans-serif"] = 'SimHei'  # 解决中文乱码
plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法正常显示的问题

df = pd.read_csv(r"C:\Users\Administrator\Desktop\python数据分析\订单.csv", encoding='utf-8')
df.set_index('订单编号', inplace=True)
df.head()
result = df.groupby('日期')['房间价格'].sum()
# 先将整个结果使用dict形式创建dataframe,再用reset_index转换列名
result1 = pd.DataFrame({"日营业额": result}).reset_index()
plt.figure(figsize=(12, 7))
x = result1['日期']
y = result1['日营业额']
plt.plot(x, y, color="k", linestyle="dashdot", linewidth=1, marker="o", markersize=5, label="日营业额")
ticks = np.array(result1['日期'])
labels = [str(i)[-2:] + '号' for i in result1['日期']]
plt.xticks(ticks, labels)
plt.title("酒店2021年7月份营业额", loc="center")
plt.xlabel('日期')
plt.ylabel('日营业额(元)')
for a, b in zip(x, y):
    plt.text(a, b, b, ha='center', va="bottom", fontsize=10)
plt.grid(True)  # 设置网格线
plt.legend()  # 设置图例，调用显示出plot中的label值
plt.show()
