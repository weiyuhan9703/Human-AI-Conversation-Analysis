# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/Iris/Desktop/chat_history.csv',header=None)
df.columns=['session_id','startTime']
df = DataFrame(df)
df['DATE'] = pd.to_datetime(df['startTime'])
df = df[['DATE','session_id']]
df['DATE'] = [datetime.strftime(x,'%Y-%m') for x in df['DATE']]
df.drop_duplicates(subset=['session_id'],keep='first',inplace=True)
print(df.head())


groups=df.groupby(['DATE']).count()
print(groups)




