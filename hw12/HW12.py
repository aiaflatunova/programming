import os
import re

def find_in_folder():
    i = 0
    file_list = os.listdir()
    for file in file_list:
        if os.path.isfile(file):
            if re.search(r'\d', file) != None:
                i += 1
    return i

print('Найдено файлов без цифр в названии: ' , find_in_folder())
