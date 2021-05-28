file_name = r'C:\Users\Iris\Desktop\delete\mix.txt'

try:
    with open(file_name, encoding='utf-8') as file_obj:
    #由于书名不是英文，要加上 encoding='utf8'
        contents = file_obj.read()
except FileNotFoundError:
    msg = 'Sorry, the file' + file_name + ' does not exist.'
    print(msg)
else:
    words = contents.rstrip()
    num_words = len(words)
    print('The file ' + file_name + ' has about ' + str(num_words) + ' words.')

#按行词语数
file_object2 = open(r'C:\Users\Iris\Desktop\delete_css.csv',encoding='UTF-8').read().split('\n')  #一行行的读取内容
space_counts = 0
number_counts = 0
number_list = []

Rs2=[] #建立存储分词的列表
for i in range(len(file_object2)):
    for line in file_object2[i]:
     line = line.strip()
     space_split_list = line.split(',')
     space_counts += len(space_split_list) - 1
    print(space_counts)

#词语数
file_name = r'C:\Users\Iris\Desktop\delete\delete_mix_stopwords.txt'

space_counts = 0
number_counts = 0
number_list = []

with open(file_name, 'r',encoding='UTF-8') as f:
    for line in f:
        line = line.strip()
        space_split_list = line.split(' ')
        space_counts += len(space_split_list) - 1
        '''for word in space_split_list:
                if word.isdigit():
                    number_list.append(word)
        number_counts = len(number_list)'''

print("space_counts", space_counts)
print("number_counts", number_counts)

from pandas import DataFrame, Series
from datetime import datetime
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
