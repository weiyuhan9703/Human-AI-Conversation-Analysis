import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
from datetime import datetime


df = pd.read_csv('C:/Users/Iris/Desktop/chat_history.csv',header=None)
df.columns=['id','session_id']
df = DataFrame(df)
df = df[['id','session_id']]
groups=df.groupby(['session_id']).count()
df_group=pd.DataFrame(groups)
print(df_group)
df_group.to_csv('C:/Users/Iris/Desktop/output3.csv')