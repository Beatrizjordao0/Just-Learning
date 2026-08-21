'''Desafio: entrar em um login da empresa e preencher todos os dados automaticamente'''
import time

#passo a passo

#importação de bibliotecas
import pyautogui as pg
import pandas as pd
import time as tm

# Passo 1 : abrir o navegador
pg.PAUSE = 0.5
pg.press('win')
pg.write('Opera')
pg.press('enter')

time.sleep(4)
# Passo 2 : entrar no site
pg.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pg.press('enter')

tm.sleep(5)
# Passo 3 : fazer o login
pg.press('tab')
pg.write('beatrizjordao15@gmail.com')
pg.press('tab')
pg.write('beatrizjordao06')
pg.press('tab')
pg.press('enter')
time.sleep(5)
# Passo 4 : preencher os produtos
#        ler o arquivo de produtos
tabela = pd.read_csv('produtos.csv')

# Preencher os produtos
#     Clico na primeira caixa e digito o item.
pg.click(x=789, y=391)


#          depois passo para a próximo e digito
#          repito para cada um e caso houver uma informação vazia eu deleto

