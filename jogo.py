import pygame
import random
from telainicial import tela_inicial
from tela_do_jogo import tela_do_jogo
from tela_gameover import tela_gameover

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((600, 500 ))
pygame.display.set_caption('Penalty')
DONE = 0
PLAYING = 1
MISSING = 2
OVER = 3
state = DONE
while state != MISSING:
    if state == DONE:
        state = tela_inicial(window)
    elif state == PLAYING:
        state = tela_do_jogo(window)
    elif state == OVER:
        state = tela_gameover(window)

# ===== Finalização =====
pygame.quit() 