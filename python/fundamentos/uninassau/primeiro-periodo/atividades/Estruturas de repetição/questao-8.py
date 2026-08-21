nmr = int(input("Digite um número para saber se é primo: "))
primo = True
if nmr < 2:
    primo = False
elif nmr == 2:
    primo = True
for n in range(2,nmr):
    if nmr % n == 0:
        primo = False

if primo == True:
    print(f"O Número {nmr} é primo.")
else:
    print(f"O Número {nmr} não é primo.")