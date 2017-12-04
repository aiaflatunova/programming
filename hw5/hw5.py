print('Input words: ')
with open("new.txt", "w", encoding="utf - 8") as f:
    word = input()
    while word != " ":
        if len(word) > 5:
            f.write(word + "\n")
        word = input()
with open("new.txt", encoding="utf - 8") as f:
    print(f.read().strip())
