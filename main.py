from operator import truediv
import pygame

pygame.init()

width, height = 750, 450
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Alien Dash')

# ufo icon
icon_surface = pygame.image.load('sprites/ufo.png')
icon = pygame.display.set_icon(icon_surface)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
