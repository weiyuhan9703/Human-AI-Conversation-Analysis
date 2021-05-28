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