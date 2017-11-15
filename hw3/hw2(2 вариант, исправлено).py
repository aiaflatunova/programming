print("Введите слово")
word = input()
for i in range((len(word)+1),2):
    if word[i] != 'о':
        if word[i] != 'п':
            if word[i] != 'е':
                print(word[i])
        
