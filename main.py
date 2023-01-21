import pygame 
FPS = 40
WIN_WIDTH = 700
WIN_HEIGHT = 500

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

game = True
play = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    clock.tick(FPS)
    pygame.display.update()
    