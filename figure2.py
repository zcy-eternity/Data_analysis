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
# 通过日营业额进行降序排序
result1 = result1.sort_values(by='日营业额', ascending=False)
# 创建新的DataFrame存放通过营业额排序后日期等于日营业额前三天数据
r2 = df[df['日期'] == result1.iat[0, 0]]
r3 = df[df['日期'] == result1.iat[1, 0]]
r4 = df[df['日期'] == result1.iat[2, 0]]
# 获取日营业额前三天每种客房对应的入住量，返回值为series类型
s2 = r2['客房类型'].value_counts()
s3 = r3['客房类型'].value_counts()
s4 = r4['客房类型'].value_counts()
# 对s3、s4的series数据重新设置索引，使其索引与s1相同
# 注reindex不改变原有对象
s3 = s3.reindex(index=s2.index)
s4 = s4.reindex(index=s2.index)
# 建立一个坐标系
plt.subplot(1, 1, 1)
# 指明x和y值
x = np.arange(len(s2.index.tolist()))
y1 = np.array(s2.values)
y2 = np.array(s3.values)
y3 = np.array(s4.values)
# 作图
plt.bar(x, y1, width=0.3, align="center", label='7月'+str(result1.iat[0, 0])[-2:]+"日")
plt.bar(x+0.3, y2, width=0.3, label='7月'+str(result1.iat[1, 0])[-2:]+"日")
plt.bar(x+0.6, y3, width=0.3, label='7月'+str(result1.iat[2, 0])[-2:]+"日")
# 设置标题
plt.title("日销售额最高的三天客房入住情况统计", loc="center")
# 添加数据标签
for a, b in zip(x, y1):
    plt.text(a, b, b, ha='center', va="bottom", fontsize=12)
for a, b in zip(x+0.3, y2):
    plt.text(a, b, b, ha='center', va="bottom", fontsize=12)
for a, b in zip(x+0.6, y3):
    plt.text(a, b, b, ha='center', va="bottom", fontsize=12)
# 设置x/y轴名称
plt.xlabel('客房种类')
plt.ylabel('入住量(间)')
# 设置x轴刻度值
plt.xticks(x+0.3, s2.index.tolist())
plt.grid(False)  # 设置网格线

plt.legend()  # 图例设置
plt.show()
