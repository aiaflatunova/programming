longest = 0
shortest = 100
with open("text.txt", encoding="utf-8") as f:
    for line in f:
        if len(line) > longest:
            longest = len(line)
        if len(line) < shortest:
            shortest = len(line)
print('Longest:', longest)
print('Shortest:', shortest)
print('Result', (shortest/longest))



