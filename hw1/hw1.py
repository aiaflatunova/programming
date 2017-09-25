print("Ведите число a: ")
a = int(input())
print("Ведите число b: ")
b = int(input())
print("Ведите число c: ")
c = int(input())
if a * b == c:
    print("c является произведенем a и b")
else:
    print("с НЕ является произведением a и b")
if c == -(b / a):
    print("c является корнем ax+b=0")
else:
    print("c НЕ является корнем ax+b=0")

