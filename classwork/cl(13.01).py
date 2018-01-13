import random
#import time
print(random)
x = random.randint(0, 10)
print(x)

a = ['мышь', 'удав', 'павлин', 'кролик', 'сова']
x = random.choice(a)
print(x)

#print(time.ctime())
print('Изначальное а', a)
random.shuffle(a)
print('Перемешанное а', a)

sub_a = random.sample(a, 2)
print(sub_a)

s = 'кибернетика'
#b = list(s)
#random.shuffle(b)
b = random.sample(s, len(s))
print(b)
s1 = ''.join(b)
#for c in b:
 #   s1 += c
print(s1)
