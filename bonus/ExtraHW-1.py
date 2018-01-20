print('Input numbers')
num = input()
list_num = []
while num != '':
    list_num.append(num)
    num = input()
s = 0
for i in range(len(list_num)):
    s = s + int(list_num[i])
average = s/len(list_num)
print('Average = ', average)
biggest = max(list_num[:])
smallest = min(list_num[:])
print('Biggest number = ', biggest)
print('Smallest number = ', smallest)
