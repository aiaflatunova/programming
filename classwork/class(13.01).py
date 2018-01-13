import random

def words_from_file(filename):
    with open(filename, encoding='utf-8') as f:
        text = f.read()
    text = text[1:] #для блокнота виндоус (удаляет ненужное начало)
    text = text.replace('.', '') 
    text = text.replace(',', '')
    text = text.lower()
    words = text.split()
    return words


def anno(word):
    a = random.sample(word, len(word))
    new_word = ''.join(a)
    return new_word


def create_csv_table(wors, table_filename, n_anno):
    with open('table.csv', 'w') as f:
        for x in words:
            f.write(x)
            for i in range(n_anno):
                f.write(';')
                f.write(anno(x))
            f.write('\n')
        
words = words_from_file('text.txt')
create_csv_table(words, 'table.csv', 3)
