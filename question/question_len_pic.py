# -*- coding:utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
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
