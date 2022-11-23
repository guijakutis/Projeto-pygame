# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

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
ball_img = pygame.transform.scale(ball_img, (65, 60))
gk_img = pygame.image.load('assets/gkparado.png').convert_alpha()
gk_img = pygame.transform.scale(gk_img, (200, 200))

# ----- Inicia estruturas de dados
game = True

gk_x = 200
gk_speedx = random.randint(-8, 8) ### ESOLHER VELOCIDADE
gk_y = 255
gk_speedy = 0

clock = pygame.time.Clock()
FPS = 30

class Ball(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        # Atualização da posição da bola
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10

class Gk(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = gk_x
        self.rect.centery = gk_y
        self.speedx = gk_speedx

    def update(self):
        # Atualização da posição do goleiro
        self.rect.x += self.speedx

        # Mantem dentro dO gol
        if self.rect.right > WIDTH - 100:
            self.rect.right = WIDTH - 100
        if self.rect.left < 50:
            self.rect.left = 50

all_sprites = pygame.sprite.Group()

ball = Ball(ball_img)
all_sprites.add(ball)
gk = Gk(gk_img)
all_sprites.add(gk)

# ===== Loop principal =====
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Atualiza
    all_sprites.update()
    gk_x += gk_speedx
    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    # Desenhando
    all_sprites.draw(window)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit() 