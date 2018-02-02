print('Input your word/phrase:')
text = input()
text.lower()
phrase = []
vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
words = text.split(' ')
for i in range(len(words)):
    one_word = list(words[i])
    for a in range(len(vowels)):
        for b in range(len(one_word)):
            if (b + 1) < len(one_word):
                if one_word[b] == vowels[a]:
                    one_word.insert(b+1, 'с' + vowels[a])
                else:
                    continue
    phrase.insert(i, ''.join(one_word))
result = ' '.join(phrase)
print(result)
