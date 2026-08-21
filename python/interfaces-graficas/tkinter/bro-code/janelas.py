#Tkinter from bro_code
'''
25/03/24
'''

from tkinter import *

window = Tk()        # cria a instância da janela

window.geometry('500x500')           # geometria da janela(tamanho e proporção)
window.title('to aprendendo TK')           # Título da janela

icon = PhotoImage(file="logo.png")     # Formata o arquivo da foto logo.png de png para photoimage
window.iconphoto(True,icon)            # adiciona a foto à janela

window.config(background='#2c403f')      # Configura a cor da tela

window.mainloop()       # chama a janela

#--------------------------------------------------------------------------------------------------------