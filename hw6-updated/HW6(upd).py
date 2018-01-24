import random
print('Вариант 2 (четырехстопный амфибрахий):')
print('----------------------------------------')
str = ''
with open('noun_m_sg.txt', encoding='utf-8') as file:
    file = file.read().split(' ')
    noun_m_sg = file
def noun_inf():
    return random.choice(noun_m_sg)

with open('preposition_gen_1s.txt', encoding='utf-8') as file:
    file = file.read().split(' ')
    prep_1syl = file
with open('preposition_gen_2s.txt', encoding='utf-8') as file:
    file = file.read().split(' ')
    prep_2syl = file
def prep_gen(syl):
    if syl == 1:
        return random.choice(prep_1syl)
    else:
        return random.choice(prep_2syl)

with open('noun_gen_m.txt', encoding='utf-8') as file:
    file = file.read().split(' ')
    noun_gm = file
with open('noun_gen_f.txt', encoding='utf-8') as file:
    file = file.read().split(' ')
    noun_gf = file
def noun_gen(gen):
    if gen == 'm':
        return random.choice(noun_gm)
    else:
        return random.choice(noun_gf)

with open('adj_gen_f.txt', encoding='utf-8') as file:
    file = file.read().split(' ')
    adj_gen_f = file
with open('adj_gen_m.txt', encoding='utf-8') as file:
    file = file.read().split(' ')
    adj_gen_m = file
def adj_gen(gen):
    if gen == 'm':
        return random.choice(adj_gen_m)
    else:
        return random.choice(adj_gen_f)

def verse_1():
    return noun_inf() + ' ' + prep_gen(2) + ' ' + noun_gen('m') + ' ' + prep_gen(1) + ' ' + noun_gen('m') + ' ' + adj_gen('m')

def verse_2():
    return noun_inf() + ' ' + prep_gen(2) + ' ' + noun_gen('f') + ' ' + prep_gen(1) + ' ' + noun_gen('f') + ' ' + adj_gen('f')

with open('gerund.txt', encoding='utf-8') as file:
    file = file.read().split(' ')
    ger = file
def gerund():
    return random.choice(ger)


with open('verb_m_past.txt', encoding='utf-8') as file:
    file = file.read().split(' ')
    verb_pst = file
def verb_past():
    return random.choice(verb_pst)


with open('noun_m_inst.txt', encoding='utf-8') as file:
    file = file.read().split(' ')
    noun_m_ins = file
with open('noun_f_inst.txt', encoding='utf-8') as file:
    file = file.read().split(' ')
    noun_f_ins = file
def noun_inst(gen):
    if gen == 'f':
        return random.choice(noun_f_ins)
    else:
        return random.choice(noun_m_ins)

with open('adj_f_inst.txt', encoding='utf-8') as file:
    file = file.read().split(' ')
    adj_f_inst = file
with open('adj_m_inst.txt', encoding='utf-8') as file:
    file = file.read().split(' ')
    adj_m_inst = file
def adj_inst(gen):
    if gen == 'f':
        return random.choice(adj_f_inst)
    else:
        return random.choice(adj_m_inst)

def verse_3():
    return gerund() + ',' + ' ' + verb_past() + ' ' + noun_inst('f') + ' ' + adj_inst('f')
def verse_4():
    return gerund() + ',' + ' ' + verb_past() + ' ' + noun_inst('m') + ' ' + adj_inst('m')
def verse_5():
    return prep_gen(1) + ' ' + noun_gen('m') + ' ' + adj_gen('m') + ' ' + adj_inst('m') + ' ' + noun_inst('m')
def verse_6():
    return prep_gen(1) + ' ' + noun_gen('f') + ' ' + adj_gen('f') + ' ' + adj_inst('f') + ' ' + noun_inst('f')

def make_verse():
    verse = random.choice([1,2,3,4,5,6])
    if verse == 1:
        return verse_1()
    elif verse == 2:
        return verse_2()
    elif verse == 3:
        return verse_3()
    elif verse == 4:
        return verse_4()
    elif verse == 5:
        return verse_5()
    else:
        return verse_6()

for n in range(4):
    print(make_verse())
