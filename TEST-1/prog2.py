with open('Extinct_languages.tsv', encoding='utf-8') as f:
    count = 0
    for line in f:
        if line.find('Critically endangered') != -1:
            count += 1
        else:
            continue
print('Critically endangered:', count)
            
