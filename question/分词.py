import jieba

fR = open(r'C:\Users\Iris\Desktop\delete\delete_css.txt', 'r', encoding='UTF-8')

sent = fR.read()
sent_list = jieba.cut(sent)

fW = open(r'C:\Users\Iris\Desktop\delete\delete_css_cut.txt', 'w', encoding='UTF-8')
fW.write(' '.join(sent_list))

fR.close()
fW.close()

