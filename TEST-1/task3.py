with open('Extinct_languages.tsv', encoding='utf-8') as f:
    print('Input languages: ')
    lang_list = []
    lang = input()
    while lang != '':
        lang_list.append(lang)
        lang = input()    
    for i in range(len(lang_list)):
        q = str(lang_list[i])
        for line in f:
            if line.find(q) != -1:
                part = line.split('\t')
                print(q, '-', part[1], '-', part[2])

                


            
            
    
    
            
