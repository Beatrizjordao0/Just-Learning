
import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#                                ***** Minha Parte ***** 

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    assinaturas = []
    for ass in range(len(as_a)):
        diferenca = abs(as_a[ass] - as_b[ass])
        assinaturas.append(diferenca)
    
    soma = 0
    for assinatura in assinaturas:
        soma += assinatura
    similaridade = soma / 6
    
    return similaridade
    

def calcula_assinatura(texto):
    wal = tam_medio_palavras(texto)
    ttr = type_token(texto)
    hlr = hapax_legomana(texto)
    sal = tam_medio_sentenca(texto)
    sac = comp_senteca(texto)
    pal = tam_medio_frase(texto)

    return [wal, ttr, hlr, sal, sac, pal]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    similaridades = []

    for texto in textos:
        assinatura = calcula_assinatura(texto)
        similaridade = compara_assinatura(assinatura, ass_cp)
        similaridades.append(similaridade)

    return similaridades.index(min(similaridades)) + 1

# ***** Tamanho Médio ***** 

def tam_medio_palavras(texto):
    soma = 0
    plvr = 0
    palavras = qntd_palavra(texto)

    for palavra in palavras:
        soma += len(palavra)
        plvr += 1
    
    media = soma / plvr

    return media

# ***** quantidade de palavras do texto *****

def qntd_palavra(texto):
    todas_palavras = []
    sentencas = separa_sentencas(texto)

    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        for frase in frases:
            palavras = separa_palavras(frase)
            todas_palavras.extend(palavras)

    return todas_palavras

# ***** Número de palavras *****

def nmr_palavras(texto):
    palavras = qntd_palavra(texto)
    p = 0

    for palavra in palavras:
        p += 1

    return p

# ***** Relação Type-Token *****

def type_token(texto):
    palavras = qntd_palavra(texto)
    palavras_dif = n_palavras_diferentes(palavras)
    p = nmr_palavras(texto)

    return palavras_dif / p

# ***** Relação Hapax-Legomana *****

def hapax_legomana(texto):
    palavras = qntd_palavra(texto)
    palavras_unicas = n_palavras_unicas(palavras)
    p = nmr_palavras(texto)

    return palavras_unicas / p

# ***** Tamanho médio de sentença *****

def tam_medio_sentenca(texto):
    sentencas = separa_sentencas(texto)
    nmr_sentenca = len(sentencas)
    nmr_caracteres = 0

    for sentenca in sentencas:
        nmr_caracteres += len(sentenca)

    return nmr_caracteres / nmr_sentenca

# *****  Complexidade de Sentença *****

def comp_senteca(texto):
    sentencas = separa_sentencas(texto)
    nmr_sentenca = len(sentencas)
    frases = 0
    for sentenca in sentencas:
        frase = separa_frases(sentenca)
        frases += len(frase)

    return frases / nmr_sentenca

# ***** Tamanho médio de frase *****

def tam_medio_frase(texto):
    frases = qntd_frases(texto)
    caracteres_frase = 0
    nmr_frase = nmr_frases(texto)
    for frase in frases:
        caracteres_frase += len(frase)

    return caracteres_frase / nmr_frase

# ***** Todas as frases de todas as sentenças *****

def qntd_frases(texto):
    todas_frases = []
    sentencas = separa_sentencas(texto)

    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        todas_frases.extend(frases)

    return todas_frases

# ***** Numero de caracteres em cada frase *****

def nmr_frases(texto):
    frases = qntd_frases(texto)
    f = 0
    for frase in frases:
        f += 1
    return f


def main():
    ass_cp = le_assinatura()

    textos = le_textos()

    similaridade = avalia_textos(textos, ass_cp)

    return f"O autor do texto {similaridade} está infectado com COH-PIAH"


print(main())
