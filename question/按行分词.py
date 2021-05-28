import jieba
import csv
file_object2=open(r'C:\Users\Iris\Desktop\mix_all_1102_text.csv',encoding='UTF-8').read().split('\n')  #一行行的读取内容
Rs2=[] #建立存储分词的列表
for i in range(len(file_object2)):
    result=[]
    seg_list = jieba.cut(file_object2[i])
    for w in seg_list :#读取每一行分词
        result.append(w)
    Rs2.append(result)#将该行分词写入列表形式的总分词列表
#写入CSV
file=open(r'C:\Users\Iris\Desktop\mix_all_1102_text_result.csv','w',encoding='UTF-8')
writer = csv.writer(file)#定义写入格式
writer.writerows(Rs2)#按行写入
#file.write(str(Rs))
file.close() 