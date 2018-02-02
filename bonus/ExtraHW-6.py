print('Input your height (in sm):')
height = int(input())
height_m = height/100
print('Input your weight (in kg):')
weight = int(input())
index = weight/(height_m * height_m)
if index <= 16:
    print('Выраженный дефицит массы тела')
elif 16 < index <= 18.5:
    print('Недостаточная (дефицит) масса тела')
elif 18.5 < index <= 24.99:
    print('Норма')
elif 24.99 < index < 30:
    print('Избыточная масса тела (предожирение)')
elif 30 <= index < 35:
    print('Ожирение первой степени')
elif 35 <= index < 40:
    print('Ожирение второй степени')
elif 40 <= index:
    print('Ожирение третьей степени (морбидное)')
