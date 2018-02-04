def extract_text(filename):
    with open(filename, encoding='utf-8') as f:
        text = str(f.read())
        text.lower()
        text.replace(',', '')
        text.replace('.', '')
        text.replace('!', '')
        text.replace(':', '')
        text.replace(';', '')
        text.replace(' -', '')
        text.replace('?', '')
        text.replace('"', '')
        text.replace('\n', '')
        words = text.split()
        return words
ness = {}
i = 0
print('Input filename:')
filename = str(input())
for word in extract_text(filename):
    if word.find('ness') != -1:
        i += 1
        if word in ness:
            ness[word] += 1
        else:
            ness[word] = 1
print('Nouns with -ness:', i)
val = list(ness.values())
num = max(val)
for key, value in ness.items():
    if value == num:
        print('Most frequent: ', key, ' - ',value)
    else:
        continue
