def read(filename):
    with open(filename, encoding='utf-8') as f:
        text = f.read()
        return text

def gr(text):
    list = text.split('\n')
    gr = []
    for i in range(len(list)):
        if list[i].find('gr') != -1:
            temp = list[i].split('"')
            gram = temp[3]
            gr.append(gram)
    return gr

def make_dict(gr):
    freq = {}
    for i in range(len(gr)):
       if gr[i] in freq:
           freq[gr[i]] += 1
       else:
           freq[gr[i]] = 1
    return freq

print('Input filename:')
filename = input()

def new_file(filename):
    text = read(filename)
    gram = gr(text)
    dictionary = make_dict(gram)
    with open('freq.txt', 'w', encoding='utf-8') as f:
        for key in dictionary:
            f.write(key)
            f.write(' - ')
            f.write(str(dictionary[key]))
            f.write('\n')

new_file(filename)
