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