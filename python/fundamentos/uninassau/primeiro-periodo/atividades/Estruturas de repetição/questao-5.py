a = 0
b = 1
for i in range(24):
    a, b = b, a+b
print(b)