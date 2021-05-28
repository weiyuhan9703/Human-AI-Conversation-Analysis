import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
from datetime import datetime


df = pd.read_csv('C:/Users/Iris/Desktop/answer.csv',header=None)
df.columns=['question_id','type']
df = DataFrame(df)
df = df[['question_id','type']]
groups=df.groupby(['question_id']).sum()
df_group=pd.DataFrame(groups)
print(df_group)
df_group.to_csv('C:/Users/Iris/Desktop/output2.csv')
