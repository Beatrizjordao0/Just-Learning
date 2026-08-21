import tkinter as tk
import random

root = tk.Tk()
root.title("Jogo do Trenzinho")

# Sentenças
sentencas_boas = [
    '4 bebês',
    'Amor da sua vida',
    'Cientista que descobriu a cura do câncer',
    'Um dinossauro bonzinho e amoroso abandonado',
    'Um menino que será adotado amanhã',
    'Um grupo de idosos'
]

sentencas_ruins = [
    'Um serial killer',
    'Professor que te reprovou na quinta série em artes',
    'Kraken atacando seu parceiro amoroso',
    'Seu chefe',
    'Cavaleiro Medieval',
    'Menino que fazia bullying com você aos 5 anos de idade'
]

escolha_boa_1 = ''
escolha_boa_2 = ''
escolha_ruim_1 = ''
escolha_ruim_2 = ''

def jogar():
    global escolha_boa_1, escolha_boa_2, escolha_ruim_1, escolha_ruim_2

    # Escolhas
    escolhas_boas = random.sample(sentencas_boas, 2)
    escolhas_ruins = random.sample(sentencas_ruins, 2)

    escolha_boa_1, escolha_boa_2 = escolhas_boas
    escolha_ruim_1, escolha_ruim_2 = escolhas_ruins

    trilho_1_label.config(text=f'Trilho 1 --> {escolha_ruim_1} e {escolha_boa_1}')
    trilho_2_label.config(text=f'Trilho 2 --> {escolha_boa_2} e {escolha_ruim_2}')

def escolher_trilho():
    escolha = int(caixa_texto.get())
    if escolha == 1:
        resultado_label.config(text=f'Você matou {escolha_ruim_1} e {escolha_boa_1}')
    elif escolha == 2:
        resultado_label.config(text=f'Você matou {escolha_ruim_2} e {escolha_boa_2}')
    else:
        resultado_label.config(text="Escolha inválida, digite 1 ou 2")

# Widgets
trilho_1_label = tk.Label(root, text='')
trilho_1_label.pack()

trilho_2_label = tk.Label(root, text='')
trilho_2_label.pack()

jogar_button = tk.Button(root, text="Jogar", command=jogar)
jogar_button.pack()

caixa_texto = tk.Entry(root, width=10)
caixa_texto.pack()

escolher_button = tk.Button(root, text="Escolher Trilho", command=escolher_trilho)
escolher_button.pack()

resultado_label = tk.Label(root, text='')
resultado_label.pack()

root.mainloop()
