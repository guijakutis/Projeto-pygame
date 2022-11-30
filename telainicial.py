import pygame
import random
from os import path

MISSING = 2
DONE = 0
PLAYING = 1


def tela_inicial(tela):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    tela = pygame.image.load('FUNDOGAME1.png').convert()
    tela.rect = tela.get_rect()
    
    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(30)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = MISSING
                running = False

            if event.type == pygame.KEYUP:
                state = DONE
                running = False

        # A cada loop, redesenha o fundo e os sprites
        tela.fill(0,0,0)
        tela.blit(tela, tela.rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state