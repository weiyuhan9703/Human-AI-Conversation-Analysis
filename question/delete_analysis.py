import re
import os

text_path = r'C:\Users\Iris\Desktop\delete'
# 拿到文件夹下面的所有文件
text_list = os.listdir(text_path)
for path in text_list:
    with open(text_path + '\\' + path,'r',encoding='UTF-8') as f:
        result = f.read()
        # 使用正则表达式去匹配标点符号
        result = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+", "",result)
        print(result)
        # result1 = demo(result)
        with open(text_path+ '\\' +path,'w',encoding='UTF-8') as w:
            w.write(str(result))