import re


def find_zone(filename):
    with open(filename, encoding='utf-8') as f:
        text = f.read()
        result = re.search(r'UTC(?:\+|-)(?:\d|\d:\d)', text)
        return result.group()


print('Input filename:')
filename = input()

print('Time zone: ', find_zone(filename))
