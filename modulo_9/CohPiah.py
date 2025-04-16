
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
    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    pass

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass

texto = "Num fabulário ainda por encontrar " \
        "será um dia lida esta fábula: A uma " \
        "bordadora dum país longínquo foi " \
        "encomendado pela sua rainha que bordasse, " \
        "sobre seda ou cetim, entre folhas, " \
        "uma rosa branca. A bordadora, como era muito jovem, " \
        "foi procurar por toda a parte aquela rosa branca " \
        "perfeitíssima, em cuja semelhança bordasse a sua. " \
        "Mas sucedia que umas rosas eram menos belas do " \
        "que lhe convinha, e que outras não eram brancas " \
        "como deviam ser. Gastou dias sobre dias, " \
        "chorosas horas, buscando a rosa que imitasse " \
        "com seda, e, como nos países longínquos nunca " \
        "deixa de haver pena de morte, ela sabia bem que, " \
        "pelas leis dos contos como este, não podiam deixar " \
        "de a matar se ela não bordasse a rosa branca. " \
        "Por fim, não tendo melhor remédio, bordou de " \
        "memória a rosa que lhe haviam exigido. " \
        "Depois de a bordar foi compará-la com as " \
        "rosas brancas que existem realmente nas roseiras. " \
        "Sucedeu que todas as rosas brancas se pareciam " \
        "exactamente com a rosa que ela bordara, que cada " \
        "uma delas era exactamente aquela. " \
        "Ela levou o trabalho ao palácio e é de " \
        "supor que casasse com o príncipe. " \
        "No fabulário, onde vem, esta fábula não " \
        "traz moralidade. Mesmo porque, na idade de ouro, " \
        "as fábulas não tinham moralidade nenhuma."

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
    caracteres = 0
    sentenca = separa_sentencas(texto)
    nmr_sentenca = len(sentenca)
    palavras = qntd_palavra(texto)
    for palavra in palavras:
        caracteres += len(palavra)
    return caracteres / nmr_sentenca

