print("Введите слово")
word = input()
i = 0
for i in range(len(word)+1):
    print(word[:i])
    i = i + 1

