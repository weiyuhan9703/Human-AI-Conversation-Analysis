import jieba

fR = open(r'C:\Users\Iris\Desktop\delete\delete_css.txt', 'r', encoding='UTF-8')

sent = fR.read()
sent_list = jieba.cut(sent)

fW = open(r'C:\Users\Iris\Desktop\delete\delete_css_cut.txt', 'w', encoding='UTF-8')
fW.write(' '.join(sent_list))

fR.close()
fW.close()

def stopwordslist():
  stopwords = [line.strip() for line in open(r'C:\Users\Iris\Desktop\stopwords.txt',encoding='UTF-8').readlines()]
  return stopwords

# 对句子进行中文分词
def seg_depart(sentence):
  # 对文档中的每一行进行中文分词
  sentence_depart = jieba.cut(sentence.strip())
  # 创建一个停用词列表
  stopwords = stopwordslist()
  # 输出结果为outstr
  outstr = ''
  # 去停用词
  for word in sentence_depart:
    if word not in stopwords:
     if word != '\t':
        outstr += word
        outstr += " "
  return outstr
file_object2 = open(r'C:\Users\Iris\Desktop\2020.11.03\3.csv').read().split('\n')  #一行行的读取内容
Rs2=[] #建立存储分词的列表
for i in range(len(file_object2)):
    result=[]
    seg_list = seg_depart(file_object2[i])

    for w in seg_list :#读取每一行分词
        result.append(w)
    Rs2.append(result)#将该行分词写入列表形式的总分词列表
#写入CSV
file=open(r'C:\Users\Iris\Desktop\2020.11.03\3_result.csv','w',encoding='UTF-8')
writer = csv.writer(file)#定义写入格式
writer.writerows(Rs2)#按行写入
#file.write(str(Rs))
file.close()

def stopwordslist():
  stopwords = [line.strip() for line in open(r'C:\Users\Iris\Desktop\stopwords.txt',encoding='UTF-8').readlines()]
  return stopwords

# 对句子进行中文分词
def seg_depart(sentence):
  # 对文档中的每一行进行中文分词
  sentence_depart = jieba.cut(sentence.strip())
  # 创建一个停用词列表
  stopwords = stopwordslist()
  # 输出结果为outstr
  outstr = ''
  # 去停用词
  for word in sentence_depart:
    if word not in stopwords:
     if word != '\t':
        outstr += word
        outstr += " "
  return outstr
file_object2 = open(r'C:\Users\Iris\Desktop\css.csv').read().split('\n')  #一行行的读取内容
Rs2=[] #建立存储分词的列表
for i in range(len(file_object2)):
    result=[]
    seg_list = seg_depart(file_object2[i])

    for w in seg_list :#读取每一行分词
        result.append(w)
    Rs2.append(result)#将该行分词写入列表形式的总分词列表
#写入CSV
file=open(r'C:\Users\Iris\Desktop\css_result1.csv','w',encoding='UTF-8')
writer = csv.writer(file)#定义写入格式
writer.writerows(Rs2)#按行写入
#file.write(str(Rs))
file.close()

#按行分词
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
