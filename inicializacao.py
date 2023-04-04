from random import randint

from constantes import *  # Você pode usar as constantes definidas em constantes.py, se achar útil
                          # Por exemplo, usar a constante CORACAO é o mesmo que colocar a string '❤'
                          # diretamente no código

import random


def gera_posicao_desocupada(posicoes_ocupadas, largura_mapa, altura_mapa):
    # Implemente esta função para o nível básico
    # A função deve retornar uma posição aleatória dentro da janela que não esteja na lista de posições ocupadas.
    # Uma posição é uma lista com exatas dois elementos: a posição x e a posição y.
    # Além disso, a posição gerada deve ser adicionada à lista de posições ocupadas.
    
    x = randint(1, largura_mapa)
    y = randint(1, altura_mapa)
    posicao = [x, y]
    while posicao in posicoes_ocupadas:
        x = randint(1, largura_mapa)
        y = randint(1, altura_mapa)
        posicao = [x, y]
    posicoes_ocupadas.append(posicao)
    return posicao


def gera_objetos(quantidade, tipo, cor, largura_mapa, altura_mapa, posicoes_ocupadas):
    """
    Esta função já está pronta, você não precisa modificá-la.

    Gera uma lista de objetos do tipo especificado, com a quantidade especificada.
    Cada objeto é um dicionário com as chaves 'tipo', 'posicao' e 'cor'.

    Parâmetros:
    quantidade: quantidade de objetos a serem gerados
    tipo: tipo do objeto a ser gerado. É uma string como '❤'
    cor: cor do objeto a ser gerado. É uma lista com três elementos, como [255, 0, 0]
    largura_mapa: largura do mapa do jogo em caracteres
    altura_mapa: altura do mapa do jogo em caracteres
    posicoes_ocupadas: lista de posições ocupadas no mapa. Cada posição é uma lista com exatamente dois elementos: a posição x e a posição y.
    """
    objetos = []

    for i in range(quantidade):
        posicao = gera_posicao_desocupada(posicoes_ocupadas, largura_mapa-1, altura_mapa-1)
        if tipo == MONSTRO:
            objetos.append({
                'tipo': tipo,
                'posicao': posicao,
                'cor': cor,
                'vidas': 5,
                'probabilidade_de_ataque': 0.3,
             })
        else:
            objetos.append({
                'tipo': tipo,
                'posicao': posicao,
                'cor': cor,
            })
    return objetos


def inicializa_estado():

    # mapa fantasma de paredes
    mapa = [[' '] * 80 for i in range(23)]
    largura_mapa = len(mapa[0])
    altura_mapa = len(mapa)

    paredes = [[PAREDE] * 80]
    linha = 1
    for linha in range(21):
        antes = randint(1, 67)
        len_parede_x = randint(5, 12)
        usado = antes + len_parede_x
        paredes.append([PAREDE] + [' '] * antes + [PAREDE] * len_parede_x + [' '] * (78 - usado) + [PAREDE])
    paredes.append([PAREDE] * 80)
    pos_jogador = [largura_mapa//2, altura_mapa//2]  # Meio do mapa
    
    # Cria outros objetos do mapa
    posicoes_ocupadas = [pos_jogador]
    objetos = []
    objetos += gera_objetos(11, CORACAO, VERMELHO, largura_mapa, altura_mapa, posicoes_ocupadas)
    objetos += gera_objetos(9, ESPINHO, VERDE_CLARO, largura_mapa, altura_mapa, posicoes_ocupadas)
    objetos += gera_objetos(6, MONSTRO, AMARELO, largura_mapa-1, altura_mapa-1, posicoes_ocupadas)
    objetos += gera_objetos(2, SHOCKWAVE, AZUL, largura_mapa, altura_mapa, posicoes_ocupadas)
    
    # faz as paredes virarem objetos reais
    x = 0
    y = 0
    for line in paredes:
        for coord in line:
            if coord == PAREDE:
                objetos.append({
            'tipo': PAREDE,
            'posicao': [x, y],
            'cor': MARROM_ESCURO,
        })
                posicoes_ocupadas.append([x,y]) # parede ocupa uma posicao
            x+=1
        x=0
        y+=1
    return {
        'tela_atual': MENU,
        'pos_jogador': pos_jogador,
        'vidas': 5,  
        'max_vidas': 5,  
        'objetos': objetos,
        'mapa': mapa,
        'mensagem': '',  
        'pos_ocupadas': posicoes_ocupadas,
        'nivel': 1,
        'xp': 0,
        'max_xp': 5
    }