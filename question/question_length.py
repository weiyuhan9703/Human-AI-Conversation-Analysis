# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/Iris/Desktop/chat_history.csv',header=None)
df.columns=['question_len','startTime']
df = DataFrame(df)
df['DATE'] = pd.to_datetime(df['startTime'])
df = df[['DATE','question_len']]
df['DATE'] = [datetime.strftime(x,'%Y-%m') for x in df['DATE']]
print(df.head())

df_sum = df.groupby('DATE')['question_len'].sum()
print(df_sum)

