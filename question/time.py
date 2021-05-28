import pandas as pd
import numpy as np
from pandas import DataFrame
import datetime
#读取数据
df = pd.read_csv('C:/Users/Iris/Desktop/chat_history.csv',header=None)
df.columns=['session_id','startTime']
df = DataFrame(df)
df['DATE'] = pd.to_datetime(df['startTime'])
df = df[['DATE','session_id']]
group =df.groupby(by='session_id')
output=group.apply(lambda x:x.max()-x.min())
print(output)
output.to_csv('C:/Users/Iris/Desktop/output.csv')




















