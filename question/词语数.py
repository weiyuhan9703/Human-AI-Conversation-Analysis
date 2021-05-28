import os
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