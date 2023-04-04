from constantes import *
import motor_grafico as motor  # Utilize as funções do arquivo motor_grafico.py para desenhar na tela
                               # Por exemplo: motor.preenche_fundo(janela, [0, 0, 0]) preenche o fundo de preto
import random

def desenha_tela(janela, estado, altura_tela, largura_tela):
    # Utilize o dicionário estado para saber onde o jogador e os outros objetos estão. 
    # Por exemplo, para saber a posição do jogador, use estado['pos_jogador']
    # O mapa esta armazenado em estado['mapa'].
    motor.preenche_fundo(janela, PRETO)
    
    altura_mapa = len(estado['mapa'])
    largura_mapa = len(estado['mapa'][0])
    borda_cima = (altura_tela - altura_mapa)//2
    borda_lado = (largura_tela - largura_mapa)//2
    for line in range(len(estado['mapa'])):
        for column in range(len(estado['mapa'][line])):
            if estado['mapa'][line][column] == ' ':
                motor.desenha_string(janela, borda_lado + column, borda_cima + line, estado['mapa'][line][column], VERDE_ESCURO, BRANCO) #desenha tela
            elif estado['mapa'][line][column] == PAREDE:
                motor.desenha_string(janela, borda_lado + column, borda_cima + line, PAREDE, MARROM_MAIS_ESCURO, MARROM_ESCURO)
    motor.mostra_janela(janela)

    for objeto in estado['objetos']:
        tipo = objeto['tipo']
        x_do_objeto = objeto['posicao'][0] + (largura_tela - largura_mapa)//2
        y_do_objeto = objeto['posicao'][1] + (altura_tela - altura_mapa)//2 
        cor = objeto['cor']
        if objeto['tipo'] == PAREDE:
            motor.desenha_string(janela, x_do_objeto, y_do_objeto, tipo, MARROM_MAIS_ESCURO, MARROM_ESCURO) # desenha as paredes
        else:
            motor.desenha_string(janela, x_do_objeto, y_do_objeto, tipo, VERDE_ESCURO, cor) # desenha os objetos
    pos_x = estado['pos_jogador'][0]  + borda_lado
    pos_y = estado['pos_jogador'][1] + borda_cima
    motor.desenha_string(janela, pos_x, pos_y, JOGADOR, PRETO, BRANCO) # desenha jogador
    
    for lost in range(estado['max_vidas']):
        motor.desenha_string(janela, lost, 2, CORACAO_BRANCO, PRETO, BRANCO)
    for vida in range(estado['vidas']):
        motor.desenha_string(janela, vida , 2, CORACAO_VERMELHO, PRETO, VERMELHO)
    motor.desenha_string(janela , 0, 0, estado['mensagem'], PRETO, BRANCO)    

    nivel = estado['nivel']
    xp_atual = estado['xp']
    max_xp = estado['max_xp']
    motor.desenha_string(janela, 0, 5, f'Nivel {nivel}', PRETO, VERDE_CLARO)
    motor.desenha_string(janela, 0, 6, f'{xp_atual} / {max_xp} XP', PRETO, VERDE_ESCURO)

def atualiza_estado(estado, tecla):
# MOVIMENTO JOGADOR
    if tecla == 'ESQUERDA':
        if estado['pos_jogador'][0] - 1 >= 0:
            estado['pos_jogador'][0] -= 1
            acao = 'left'
    elif tecla == "DIREITA":
        if estado['pos_jogador'][0] + 1 < len(estado['mapa'][0]):
            estado['pos_jogador'][0] += 1
            acao = 'right'
    elif tecla == 'CIMA':
        if estado['pos_jogador'][1] - 1 >= 0:
            estado['pos_jogador'][1] -= 1
            acao = 'up'
    elif tecla == 'BAIXO':
        if estado['pos_jogador'][1] + 1 < len(estado['mapa']):
            estado['pos_jogador'][1] += 1
            acao = 'down'

    estado['mensagem'] = ''

    for objeto in estado['objetos']:
# INTERACOES COM O MUNDO    
        if estado['pos_jogador'] == objeto['posicao']:
    # MECANICA CORACAO
            if objeto['tipo'] == CORACAO:
                if estado['vidas'] < estado['max_vidas']:
                    estado['vidas'] += 1
                    estado['mensagem'] = 'LESGOOO  +1 life!'
                    estado['objetos'].remove(objeto)
    # MECANICA ESPINHO
            elif objeto['tipo'] == ESPINHO:
                estado['vidas'] -= 1
                estado['mensagem'] = 'OUCH!!  -1 life'
                if estado['vidas'] == 0:
                    estado['tela_atual'] = GAME_OVER
# MECANICA PAREDE
    #   JOGADOR                 
            elif objeto['tipo'] == PAREDE:
                if acao == 'left':
                    estado['pos_jogador'][0] += 1
                elif acao == 'right':
                    estado['pos_jogador'][0] -= 1
                elif acao == 'up':
                    estado['pos_jogador'][1] += 1
                elif acao == 'down':
                    estado['pos_jogador'][1] -= 1
                estado['mensagem'] = 'quantum tunneling failed!'
# MECANICA MONSTRO COMPLETA                
    #   MONSTRO        
            elif objeto['tipo'] == MONSTRO:
                if acao == 'left':
                    estado['pos_jogador'][0] += 1
                elif acao == 'right':
                    estado['pos_jogador'][0] -= 1
                elif acao == 'up':
                    estado['pos_jogador'][1] += 1
                elif acao == 'down':
                    estado['pos_jogador'][1] -= 1
    # COMBATE COM MONSTRO
                if random.random() < 0.3: 
                    estado['vidas'] -= 1
                    if estado['vidas'] == 0:
                        estado['tela_atual'] = GAME_OVER
                    estado['mensagem'] = 'you were atacked!! -1 life'
                else:
                    objeto['vidas'] -= 1
                    mon_lifes = objeto['vidas']
                    if objeto['vidas'] <= 0:
                        estado['pos_jogador'] = objeto['posicao']
                        estado['objetos'].remove(objeto)
                        estado['mensagem'] = 'you killed the monster!!'
                # NIVEL DE XP
                        if estado['xp']+5 < estado['max_xp']:
                            estado['xp']+=5
                        else:
                            estado['xp']=0
                            estado['nivel']+=1
                            estado['max_xp']+=5
                            estado['max_vidas']+=1
                            estado['mensagem'] = 'Level UP!!'
                    else:
                        estado['mensagem'] = f'nice hit!! the monster has {mon_lifes} lifes left'
    # MOVIMENTO MONSTRO
        if objeto['tipo'] == MONSTRO:
            vectors = ['cima', 'baixo', 'esquerda', 'direita']
            direcao = random.choice(vectors) # sorteia uma direcao
            if direcao == 'cima':
                new_mon_position = [objeto['posicao'][0], objeto['posicao'][1] + 1]
                if new_mon_position not in estado['pos_ocupadas'] and new_mon_position != estado['pos_jogador']:
                    objeto['posicao'] = new_mon_position
            elif direcao == 'baixo':
                new_mon_position = [objeto['posicao'][0], objeto['posicao'][1] - 1]
                if new_mon_position not in estado['pos_ocupadas'] and new_mon_position != estado['pos_jogador']:
                    objeto['posicao'] = new_mon_position
            elif direcao == 'esquerda':
                new_mon_position = [objeto['posicao'][0] + 1, objeto['posicao'][1]]
                if new_mon_position not in estado['pos_ocupadas'] and new_mon_position != estado['pos_jogador']:
                    objeto['posicao'] = new_mon_position
            elif direcao == 'direita':
                new_mon_position = [objeto['posicao'][0] - 1, objeto['posicao'][1]]
                if new_mon_position not in estado['pos_ocupadas'] and new_mon_position != estado['pos_jogador']:
                    objeto['posicao'] = new_mon_position
    
    # Ao apertar a tecla 'i', o jogador deve ver o inventário
    if tecla == 'i':
        estado['tela_atual'] = TELA_INVENTARIO
    # Termina o jogo se o jogador apertar ESC ou 'q'
    elif tecla == motor.ESCAPE or tecla =='q':
        estado['tela_atual'] = SAIR

        #123