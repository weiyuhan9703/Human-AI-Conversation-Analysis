# -*- coding:utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
from datetime import datetime
import numpy as np
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
# 构建数据
x = ['1701','1702','1703','1704','1705','1706','1707','1708','1709','1710','1711','1712',
     '1801','1802','1803','1804','1805','1806','1807','1808','1809','1810','1811','1812']
y = [58,53,52,32,53,56,59,59,54,19,65,51,42,46,43,44,45,45,49,41,41,42,44,47]

# 设置画布大小

plt.figure(figsize=(16, 4))

# 标题

plt.title("平均session长度")

# 数据

plt.plot(x, y, linewidth=3, color='r', marker='o',

         markerfacecolor='white', markersize=10)

# 横坐标描述

plt.xlabel('month')

# 纵坐标描述

plt.ylabel('avg_len')

# 设置数字标签

for a, b in zip(x, y):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

plt.legend()

plt.show()

# number of questions
df = pd.read_csv('C:/Users/Iris/Desktop/chat_history.csv',header=None)
df.columns=['id','session_id']
df = DataFrame(df)
df = df[['id','session_id']]
groups=df.groupby(['session_id']).count()
df_group=pd.DataFrame(groups)
print(df_group)
df_group.to_csv('C:/Users/Iris/Desktop/output3.csv')

#length of questions
df = pd.read_csv('C:/Users/Iris/Desktop/chat_history.csv',header=None)
df.columns=['question_len','startTime']
df = DataFrame(df)
df['DATE'] = pd.to_datetime(df['startTime'])
df = df[['DATE','question_len']]
df['DATE'] = [datetime.strftime(x,'%Y-%m') for x in df['DATE']]
print(df.head())

df_sum = df.groupby('DATE')['question_len'].sum()
print(df_sum)

#session

# 构建数据
x = ['2017-01','2017-02','2017-03','2017-04','2017-05','2017-06','2017-07','2017-08','2017-09','2017-10','2017-11','2017-12',
     '2018-01','2018-02','2018-03','2018-04','2018-05','2018-06','2018-07','2018-08','2018-09','2018-10','2018-11','2018-12']
y = [523,353,423,461,2040,1737,1636,1336,1114,5753,19666,19330,33726,1188,7804,2980,1592,1215,1127,1076,5971,2452,1689,1752]
# 绘图
plt.bar(x=x, height=y, label='时间', color='steelblue', alpha=0.8)
# 在柱状图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
for x1, yy in zip(x, y):
    plt.text(x1, yy + 1, str(yy), ha='center', va='bottom', fontsize=6, rotation=0)
# 设置标题
plt.title("2017-2018会话数量统计")
# 为两条坐标轴设置名称
plt.xlabel("时间")
plt.ylabel("会话数量")
# 显示图例
plt.legend()
# 画折线图
plt.plot(x, y, "r", marker='*', ms=10, label="会话数量")
plt.xticks(rotation=45)
plt.legend(loc="upper left")
plt.savefig("C:/Users/Iris/Desktop/a.jpg")
plt.show()

