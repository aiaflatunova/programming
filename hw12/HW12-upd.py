import os
import re

def find_in_folder():
    i = 0
    file_list = os.listdir()
    print('Файлы в папке')
    for file in file_list:
        print(file)
        if os.path.isfile(file):
            if re.search(r'\d', file) != None:
                i += 1
    print('\nНайдено файлов без цифр в названии:', i)


print(find_in_folder())
