'''
salario = float(input('Digite um valor para um salário:\n'))
aumento = 5/100 * salario

print('SEU NOVO SALÁRIO É: ',aumento + salario)

'''
'''
numero = int(input('Digite um número afim de ganhar uma tabuada do mesmo:\n'))

for i in range(1,11):
    print(numero * i, end=",")
'''

from tkinter import *

janela = Tk()

label = Label(janela,
              text=('Jesus saves, bro!'),
              bg='#FF00FF',
              font=('Arial',150))
label.pack()



janela.mainloop()




a = int(input(''))