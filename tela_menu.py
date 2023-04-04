from constantes import *
import motor_grafico as motor

def desenha_menu(janela, estado, altura_tela, largura_tela):

    roguelike_101 = ''' 
 ____                                    ___        __                     _     __      _     
/\  _`\                                 /\_ \    __/\ \                  /' \  /'__`\  /' \    
\ \ \L\ \    ___      __   __  __     __\//\ \  /\_\ \ \/'\      __     /\_, \/\ \/\ \/\_, \   
 \ \ ,  /   / __`\  /'_ `\/\ \/\ \  /'__`\\ \ \ \/\ \ \ , <    /'__`\   \/_/\ \ \ \ \ \/_/\ \  
  \ \ \\ \ /\ \L\ \/\ \L\ \ \ \_\ \/\  __/ \_\ \_\ \ \ \ \\`\ /\  __/      \ \ \ \ \_\ \ \ \ \ 
   \ \_\ \_\ \____/\ \____ \ \____/\ \____\/\____\\ \_\ \_\ \_\ \____\      \ \_\ \____/  \ \_\                                                    
                      \_/__/                                                                   '''
    
    motor.preenche_fundo(janela, PRETO)

    motor.desenha_string(janela, 1, 1, roguelike_101, PRETO, BRANCO)
    motor.desenha_string(janela, 5, 12, 'press (p) to play', PRETO, BRANCO)
    motor.desenha_string(janela, 5, 13, 'press (h) for instructions', PRETO, BRANCO)

def atualiza_estado(estado, tecla):
    estado['tela_atual'] == MENU
    if tecla == 'p':
        estado['tela_atual'] = TELA_JOGO
    elif tecla == 'q':
        estado['tela_atual'] = SAIR
    elif tecla == 'h':
        estado['tela_atual'] = HELP