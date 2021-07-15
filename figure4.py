# %config InlineBackend.figure_format = 'svg'
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams["font.sans-serif"] = 'SimHei'  # 解决中文乱码
plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法正常显示的问题

df = pd.read_csv(r"C:\Users\Administrator\Desktop\python数据分析\订单.csv", encoding='utf-8')
df.set_index('订单编号', inplace=True)
df.head()
result = df.groupby(['日期', '客房类型'])
print(result.get_group((20210721, '大床房'))['客房类型'].count())
ls = []
new_df = pd.DataFrame(columns=['精致套房', '套房', '钟点房', '普通标间', '大床房'])
for i in range(31):
    ls.append(result.get_group((20210700 + i + 1, '精致套房'))['客房类型'].count())
    ls.append(result.get_group((20210700 + i + 1, '套房'))['客房类型'].count())
    ls.append(result.get_group((20210700 + i + 1, '钟点房'))['客房类型'].count())
    ls.append(result.get_group((20210700 + i + 1, '普通标间'))['客房类型'].count())
    ls.append(result.get_group((20210700 + i + 1, '大床房'))['客房类型'].count())
    new_df.loc[i] = dict(zip(['精致套房', '套房', '钟点房', '普通标间', '大床房'], ls))
    ls = []
print(new_df)
x = np.arange(1, 32)
y1 = new_df["精致套房"]
y2 = new_df["套房"]
y3 = new_df["钟点房"]
y4 = new_df["普通标间"]
y5 = new_df["大床房"]
plt.figure()
plt.plot(x, y1, label="精致套房")
plt.plot(x, y2, label="套房")
plt.plot(x, y3, label="钟点房")
plt.plot(x, y4, label="普通标间")
plt.plot(x, y5, label="大床房")
plt.legend(loc='upper right')
plt.title("七月各种客房入住情况统计")
plt.xlabel("日期")
plt.ylabel("入住量")
plt.show()
