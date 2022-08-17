import pygame

WIDTH = 1200
HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprite/Run_000.png')
        self.rect = pygame.Rect(100, 100, 100, 100)

pygame.init()
game_window =pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption('Jogo 01')

gameloop = True

def draw():
    game_window.fill(255, 255, 0)

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            break
    draw()
    pygame.display.update()
