with open('Extinct_languages.tsv', encoding='utf-8') as f:
    print('Input languages: ')
    lang_list = []
    lang = input()
    while lang != '':
        lang_list.append(lang)
        lang = input()    
    for i in range(len(lang_list)):
        print(lang_list[i])
        ask = str(lang_list[i])
        for line in f:
            if line.find(ask) != -1:
                print('yes')
                #part = line.split('\t')
                #print(ask, '-', part[1], '-', part[2])
            #else:
                #continue


            
            
    
    
            
