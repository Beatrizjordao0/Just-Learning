# Tkinter from Bro_code
'''
25/03/24
'''

from tkinter import *

wd = Tk()

#       labels

'''
TODA FOTO QUE EU FOR USAR TEM QUE ESTAR NO MESMO DIRETÓRIO DO ARQUIVO PYTHON
OU EU TENHO QUE PASSAR O CAMINHO DA FOTO.
'''

foto = PhotoImage(file='computador.png')        #Foto que eu escolhi. 


caixa = Label(wd,                  # caixa para texto dentro da janela window
              text='Lets code?',            # texto dentro da label
              font=('Arial',40,'bold'),         # fonte, tamanho e estilo
              fg='#511799',                  # cor do texto 
              bg='#140469',               # cor da parte de tras do texto
              relief= RAISED,          # estilo da borda da caixa de texto 
              bd=30,           # tamanho da borda
              padx=20,      # distância do texto para a borda horizontalmente
              pady=20,          # ''    ''  ''    '' ''  ''   verticalmente
              image=foto,       # adiciona a imagem à caixa de texto 
              compound='bottom')      # Diz aonde a fot vai ficar em relação ao texto    


# caixa.place(x=600,y=350)       # Não preciso do caixa.pack() quando uso o place
caixa.pack()         # compila e confirma a presença do texto na janela window




wd.mainloop()

