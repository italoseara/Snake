import pygame
import random
from pygame.locals import *


def on_grid_random():
    x = random.randint(0, 790)
    y = random.randint(0, 590)
    return x // 20 * 20, y // 20 * 20


def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake')
icon = pygame.image.load('icon.bmp')
pygame.display.set_icon(icon)

snake = [(200, 200), (220, 200), (230, 200)]
snake_skin = pygame.Surface((20, 20))
snake_skin.fill((255, 255, 255))

apple_pos = on_grid_random()
apple = pygame.image.load('apple.bmp')

my_direction = LEFT

clock = pygame.time.Clock()

tick = 10
count = 0
points = 0

while True:
    clock.tick(tick)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.QUIT()

    if event.type == KEYDOWN:
        if event.key == K_UP:
            my_direction = UP
        if event.key == K_DOWN:
            my_direction = DOWN
        if event.key == K_LEFT:
            my_direction = LEFT
        if event.key == K_RIGHT:
            my_direction = RIGHT

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    for d in range(2, len(snake)):
        if count < 1:
            count += 1
            
        elif snake[0] == snake[d]:
            print('\033[1;31mGAME OVER\033[m')
            print(f'\033[1;34mYou ate {points} Apples!\033[m')
            exit()

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))
        if tick <= 25:
            tick += 0.5
        points += 1

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 20)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 20)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 20, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 20, snake[0][1])

    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)

    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()
