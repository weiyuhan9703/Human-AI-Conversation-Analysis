import pandas as pd
import numpy as np
from pandas import DataFrame, Series
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt
pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)


df = pd.read_csv('C:/Users/Iris/Desktop/chat_history1.csv',header=None)
df.columns=['id','classify']
df = DataFrame(df)

# number of classification
pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)


df = pd.read_csv('C:/Users/Iris/Desktop/chat_history1.csv',header=None)
df.columns=['id','classify']
df = DataFrame(df)

df_count=df['classify'].value_counts()
print(df_count)
outputpath='C:/Users/Iris/Desktop/classify_count.csv'
df_count.to_csv(outputpath,sep=',',index=False,header=False)

#pic
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']='SimHei'#设置中文显示

plt.figure(figsize=(12,8))#将画布设定为正方形，则绘制的饼图是正圆

label=['其他','带病投保','投保年龄','平台','保费/价格','免赔额','理赔','问候语','微医保','社保知识','续保','疾病范围','家庭/家人','投保','体检/健康告知'
       ,'报销范围','定点医院','操作','泰康','住院','保单/合同','保额','门诊费','免责条款','产品责任','微保','停售/下架','竞品','月缴','社保','其余不足1%']#定义饼图的标签，标签是列表

explode=[0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01
         ,0.01,0.01,0.01,0.01,0.01,0.01,0.01]#设定各项距离圆心n个半径

#plt.pie(values[-1,3:6],explode=explode,labels=label,autopct='%1.1f%%')#绘制饼图

values=[0.39,0.06,0.05,0.04,0.04,0.03,0.03,0.03,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01
        ,0.01,0.01,0.01,0.01,0.01,0.04]

plt.pie(values,explode=explode,labels=label,autopct='%1.1f%%',shadow=False,pctdistance=0.8,startangle=90,textprops={'fontsize':15,'color':'w'})#绘制饼图

plt.title('question类型分布图')
plt.axis('equal')
plt.legend(loc='upper right')
plt.savefig('C:/Users/Iris/Desktop/classify.png', dpi=600)
plt.show()
