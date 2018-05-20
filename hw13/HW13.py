import os
import re


def extract_names():
    names = []
    start_path = '.'
    for path, dirs, files in os.walk(start_path):
        if len(dirs) != 0:
            for name in dirs:
                print(name)
                names.append(str(name))
    return names


def match_alphabet(names):
    cyr = []
    for name in names:
        if re.search(r'[^а-яёА-Я\s]', name) is None:
            cyr.append(name)
    return cyr


def fin():
    names = extract_names()
    cyr = match_alphabet(names)
    return len(cyr)


print('Number of directories with a cyrillic name: ', fin())
