import re

def word_freq(output):
    freq = {}
    for i in range(len(output)):
       if output[i] in freq:
           freq[output[i]] += 1
       else:
           freq[output[i]] = 1
    return freq


def find_in_file(filename):
    with open(filename, encoding='utf-8') as f:
        text = f.read()
        text = text.lower()
        forms = r'(найд(?:у|ут|ешь|ёшь|ет|ёт|ете|ёте|ем|ём|ите|я|и|енный|енным|енныё|енных|енными|енного|енной|енному|енном|енноё|енную)|наш(?:ел|ёл|ла|ли|ло|едший|едшая|едшее|едшие|едшим|едщих|едшими|едшего|едшему|едшей|едшую|едшим|едщими|едшем)|найти)'
        output = re.findall(forms, text)
        if output == []:
            return 'В файле не найдено форм глагола "найти"'
        else:
            return word_freq(output)




print('Input filename:')
filename = input()
print(find_in_file(filename))
