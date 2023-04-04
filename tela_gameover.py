from constantes import *
import motor_grafico as motor

def desenha_gameover(janela, estado, altura_tela, largura_tela):
    motor.preenche_fundo(janela, PRETO)
    x_center = largura_tela//2
    y_center = altura_tela//2
    motor.desenha_string(janela, x_center + 28, y_center, '--->  GAME OVER  <---', PRETO, BRANCO)
    motor.desenha_string(janela, x_center + 30, y_center + 2, 'press (q) to exit', PRETO, BRANCO)

def atualiza_estado(estado, tecla):
    estado['tela_atual'] = GAME_OVER
    if tecla in (motor.ESCAPE, 'q'):
        estado['tela_atual'] = SAIR