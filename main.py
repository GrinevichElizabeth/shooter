import pygame
import os
pygame.init()


def path_file(file_name):
    folder_path = os.path.abspath(__file__ + "/..")
    path = os.path.join(folder_path, file_name)
    return path

FPS = 40
WIN_WIDTH = 700
WIN_HEIGHT = 500

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

background = pygame.image.load(path_file("background.jpg"))
background = pygame.transform.scale(background, (WIN_WIDTH, WIN_HEIGHT))

pygame.mixer.music.load(path_file("main_song.mp3"))
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

game = True
play = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if play == True:
        window.blit(background, (0, 0))

    clock.tick(FPS)
    pygame.display.update()
    