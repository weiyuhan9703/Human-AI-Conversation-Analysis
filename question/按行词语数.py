import csv
import jieba
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
