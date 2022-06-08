
import pygame

from Escolha_de_Fase import  escolha_de_fase
from Fase_3 import fase3
from Fase_classica import fase2
from Game_over import gameover
from fase_do_mario import fase1

from tela_inicio import tela_de_inicio

pygame.init()


WIDTH = 960
HEIGHT = 1023
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('BREAKING BRICKS')

STATE = 'inicio'
while STATE != 'QUIT':
    if STATE == 'inicio':
        STATE = tela_de_inicio(window)
    elif STATE == 'escolha_fase':
        STATE = escolha_de_fase(window)
    elif STATE =='Fase_1':
        STATE = fase1(window)
    elif STATE == 'Fase_2':
        STATE = fase2(window)
    elif STATE == 'Fase_3':
        STATE = fase3(window)
    elif STATE == 'Game_over':
        STATE = gameover(window)
    else:
        STATE = 'QUIT'


# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados