import os
import re

dirpath = './news'
list = []
for filename in os.listdir(dirpath):
    filepath = os.path.join(dirpath, filename)
    with open(filepath, encoding='utf-8') as f:
        text = f.read()
        text = text.replace("`", '')
        result = re.search(r'<title>(?:.*)</title>', text)
        result = result.group()
        result = result.replace('<title>', '')
        result = result.split('//')
        title = result[0]
        filename = filename.split('.')[0]
        filename = filename + '.txt'
        filepath = os.path.join(dirpath, filename)

        with open(filepath, "w", encoding="cp1251") as nf:
            nf.write(title)
            nf.write('\n')




