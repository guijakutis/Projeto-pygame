# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from pygame import *
import random
import math

pygame.init()

# ----- Gera tela principal
WIDTH = 600
HEIGHT = 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hello World!')

# ----- Inicia assets
background = pygame.image.load('assets/gol.jpg').convert()
background = pygame.transform.scale(background, (600, 550))
ball_img = pygame.image.load('assets/soccerball.png').convert_alpha()
ball_img = pygame.transform.scale(ball_img, (55, 50))
aim_img = pygame.image.load('assets/aim.png').convert_alpha()
aim_img = pygame.transform.scale(aim_img, (50, 50))
gk_img = pygame.image.load('assets/gkparado.png').convert_alpha()
gk_img = pygame.transform.scale(gk_img, (200, 200))
gkaltodir_img = pygame.image.load('assets/gkaltodir.png').convert_alpha()
gkaltodir_img = pygame.transform.scale(gkaltodir_img, (200, 200))
gkaltoesq_img = pygame.image.load('assets/gkaltoesq.png').convert_alpha()
gkaltoesq_img = pygame.transform.scale(gkaltoesq_img, (200, 200))
gkbaixodir_img = pygame.image.load('assets/gkbaixodir.png').convert_alpha()
gkbaixodir_img = pygame.transform.scale(gkbaixodir_img, (200, 200))
gkbaixoesq_img = pygame.image.load('assets/gkbaixoesq.png').convert_alpha()
gkbaixoesq_img = pygame.transform.scale(gkbaixoesq_img, (200, 200))
gkaltomeio_img = pygame.image.load('assets/gkaltomeio.png').convert_alpha()
gkaltomeio_img = pygame.transform.scale(gkaltomeio_img, (200, 200))
gkbaixomeio_img = pygame.image.load('assets/gkbaixomeio.png').convert_alpha()
gkbaixomeio_img = pygame.transform.scale(gkbaixomeio_img, (200, 200))


# ----- Inicia estruturas de dados
game = True

gk_x = 280
gk_y = 255
gk_speedx = 0
gk_speedy = 0
aim_x = 255
aim_y = 255
aim_speedx = 0
aim_speedy = 0
ball_x = 255
ball_y = 255
ball_speedx = 0
ball_speedy = 0

clock = pygame.time.Clock()
FPS = 30

class Aim(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):
        # Atualização da posição da bola
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0


class Gk(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = gk_x
        self.rect.centery = gk_y
        self.speedx = gk_speedx
        self.speedy = gk_speedy

    def update(self):
        # Atualização da posição do goleiro
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Mantem dentro dO gol
        if self.rect.right > WIDTH - 86:
            self.rect.right = WIDTH - 86
        if self.rect.left < 50:
            self.rect.left = 50
        if self.rect.top < 102:
            self.rect.top = 102
        if self.rect.bottom > 350:
            self.rect.bottom = 350

class Ball(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = ball_speedx
        self.speedy = ball_speedy

    def update(self):
        # Atualização da posição da bola
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

all_sprites = pygame.sprite.Group()

gk = Gk(gk_img)
all_sprites.add(gk)
ball = Ball(ball_img)
all_sprites.add(ball)
aim = Aim(aim_img)
all_sprites.add(aim)

# ===== Loop principal =====
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_UP:
                aim.speedy -= 10
            if event.key == pygame.K_DOWN:
                aim.speedy += 10
            if event.key == pygame.K_LEFT:
                aim.speedx -= 10
            if event.key == pygame.K_RIGHT:
                aim.speedx += 10
            if event.key == pygame.K_SPACE:
                ball.speedx = aim_x - 255
                ball.speedy = aim_y - 255
                gk.speedx = random.randint(-7, 7) 
                gk.speedy = random.randint(-4, 4)
                
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_UP:
                aim.speedy += 10
            if event.key == pygame.K_DOWN:
                aim.speedy -= 10            
            if event.key == pygame.K_LEFT:
                aim.speedx += 10
            if event.key == pygame.K_RIGHT:
                aim.speedx -= 10

    # ----- Atualiza
    all_sprites.update()

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    # Desenhando
    all_sprites.draw(window)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit() 