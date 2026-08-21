a = 0
b = 1
print(a)
print(b)
for i in range(101):
    a, b = b, a+b
    print(b)