from constantes import *
import motor_grafico as motor

def desenha_help(janela, estado, altura, largura):
    motor.preenche_fundo(janela, PRETO)

    full_text = '''
    Disclaimer: This is a roguelike game created in python with the goal of learning game development skills. It is not meant to be a competitive game.
    
    Gameplay: In this game, your character is a @ symbol with 5 life. You should avoid the # symbols, 
    they are spikes that deal a damage of 1 heart each time the character passes though.
    The monsters walk one square in a random direction every time you move, it is possible to battle them by trying to go though them.
    
    Keybinds: 

    (i) - Access inventory
    (q)/(esc) - Quit the game
    (arrows) - Move the payer
    (p) - Play the game'''

    motor.desenha_string(janela, 1, 1, full_text, PRETO, BRANCO)
    motor.mostra_janela(janela)

def atualiza_estado(estado, tecla_apertada):
    estado['tela_atual'] == HELP
    if tecla_apertada == 'q':
        estado['tela_atual'] = SAIR
    elif tecla_apertada == 'p':
        estado['tela_atual'] = TELA_JOGO
