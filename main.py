# coding: utf-8

# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.

import csv

# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
#
def q_1():
    arquivo = open('data.csv', encoding='utf-8', mode='r')
    reader = csv.DictReader(arquivo)

    nacionalidade = ''
    quant_nac = 0
    set_nacionalidades = set()

    for linha in reader:
        nacionalidade = linha['nationality']
        set_nacionalidades.add(nacionalidade)

    quant_nac = len(set_nacionalidades)

    arquivo.close()

    return quant_nac


# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
#
def q_2():
    arquivo = open('data.csv', encoding='utf-8', mode='r')
    reader = csv.DictReader(arquivo)

    clube = ''
    quant_club = 0
    set_clubes = set()
    
    for linha in reader:
        clube = linha['club']
        set_clubes.add(clube)

    quant_club = len(set_clubes)

    arquivo.close()

    return quant_club


# **Q3.** Liste o primeiro nome dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
    arquivo = open('data.csv', encoding='utf-8', mode='r')
    reader = csv.DictReader(arquivo)

    lista_nomes = []
    nome = ''
    x = 0
    
    for linha in reader:
        nome = linha['full_name']
        lista_nomes.append(nome)
        x += 1

        if  x == 20:
            break

    arquivo.close()

    return lista_nomes


# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    arquivo = open('data.csv', encoding='utf-8', mode='r')
    reader = csv.DictReader(arquivo)

    lista_top_ten = []
    nome = ''
    x = 0
    
    data = sorted(reader, key=lambda row: (float(row['eur_wage'])), reverse=True)
    for eachrow in data:
        nome = eachrow['full_name']
        lista_top_ten.append(nome)
        x += 1

        if  x == 10:
            break

    arquivo.close()

    return lista_top_ten


# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
    arquivo = open('data.csv', encoding='utf-8', mode='r')
    reader = csv.DictReader(arquivo)

    lista_top_ten = []
    nome = ''
    x = 0
    
    data = sorted(reader, key=lambda row: (int(row['age'])), reverse=True)
    for eachrow in data:
        nome = eachrow['full_name']
        lista_top_ten.append(nome)
        x += 1

        if  x == 10:
            break

    arquivo.close()

    return lista_top_ten


# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    arquivo = open('data.csv', encoding='utf-8', mode='r')
    reader = csv.DictReader(arquivo)

    dict_idades_val = {}
    qtde_idade = 0
    idade = 0
    idadeAnt = 0
    
    data = sorted(reader, key=lambda row: (int(row['age'])))
    for eachrow in data:
        idade = eachrow['age']

        if  idadeAnt != 0 and idade != idadeAnt:
            dict_idades_val.update({int(idadeAnt):qtde_idade})
            qtde_idade = 0

        idadeAnt = idade
        qtde_idade += 1

    if  idade == idadeAnt:
        dict_idades_val.update({int(idadeAnt):qtde_idade})

    arquivo.close()

    return dict_idades_val


