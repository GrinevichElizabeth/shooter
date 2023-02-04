import pygame
import os
from random import randint
pygame.init()


def path_file(file_name):
    folder_path = os.path.abspath(__file__ + "/..")
    path = os.path.join(folder_path, file_name)
    return path

FPS = 40
WIN_WIDTH = 700
WIN_HEIGHT = 500
WHITE = (255, 255, 255)

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

background = pygame.image.load(path_file("background.jpg"))
background = pygame.transform.scale(background, (WIN_WIDTH, WIN_HEIGHT))

pygame.mixer.music.load(path_file("main_song.mp3"))
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, width, height, speed):
        super().__init__()
        self.image = pygame.image.load(path_file(image))
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, image, x, y, width, height, speed):
        super().__init__(image, x, y, width, height, speed)
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
    def fire(self):
        pass


class Enemy(GameSprite):
    def __init__(self, image, x, y, width, height, speed):
        super().__init__(image, x, y, width, height, speed)

    def update(self):
        global missed_enemies
        self.rect.y += self.speed
        if self.rect.y >= WIN_HEIGHT:
            self.rect.bottom = 0
            self.rect.x = randint(0, WIN_WIDTH - self.rect.width)
            self.speed = randint(1, 3)
            missed_enemies += 1
        

#! 1 - картинка, 2 - х, 3 - у, 4 - размер х, 5 - размер у, 6 - скорость
player = Player(path_file("player.png"), 300, 400, 70, 100, 5)
enemies = pygame.sprite.Group()

for i in range(5):
    enemy = Enemy(path_file('enemy1.png'), randint(0, WIN_WIDTH - 50), 0, 50, 50, randint(1, 3))
    enemies.add(enemy)

missed_enemies = 0
killed_enemies = 0
font = pygame.font.SysFont("arial", 25, 0, 0)
txt_missed = font.render("Пропущено: " + str(missed_enemies), True, WHITE)
txt_killed = font.render("Убито: " + str(killed_enemies), True, WHITE)

game = True
play = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if play == True:
        window.blit(background, (0, 0))

        txt_missed = font.render("Пропущено: " + str(missed_enemies), True, WHITE)
        txt_killed = font.render("Убито: " + str(killed_enemies), True, WHITE)
        window.blit(txt_missed, (10, 50))
        window.blit(txt_killed, (10, 75))

        player.reset()
        player.update()

        enemies.draw(window)
        enemies.update()

    clock.tick(FPS)
    pygame.display.update()
    