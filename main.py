import pygame

pygame.init()

width, height = 750, 450
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Alien Dash')
clock = pygame.time.Clock()

# ufo icon
icon_surface = pygame.image.load('sprites/ufo.png')
icon = pygame.display.set_icon(icon_surface)

# player
player_surface = pygame.image.load('sprites/player.png')
x_position = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    x_position += 1
    screen.blit(player_surface,(x_position,0))


    pygame.display.update()
    clock.tick(60)