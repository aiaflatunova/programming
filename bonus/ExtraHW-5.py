print('Input your word/phrase:')
text = input()
text.lower()
phrase = []
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
words = text.split(' ')
print(words)
for i in range(len(words)):
    one_word = list(words[i])
    for a in range(len(consonants)):
        for b in range(len(one_word)):
            if one_word[b] == consonants[a] and b != (len(one_word)-1):
                one_word.insert(b+1, 'aig')
            else:
                continue
    phrase.insert(i, ''.join(one_word))
result = ' '.join(phrase)
print(result)