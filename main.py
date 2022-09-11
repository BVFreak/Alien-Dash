import pygame, sys

# initialize pygame
pygame.init()

screen = pygame.display.set_mode((750, 450))
pygame.display.set_caption('Alien Dash')
clock = pygame.time.Clock()

# icon
icon = pygame.image.load('sprites/ufo.png')
icon_surface = pygame.display.set_icon(icon)

# ground
ground_surface = pygame.image.load('sprites/cobblestone.png').convert()

# player

x_increment = 4
y_increment = 1
player_surface = pygame.image.load('sprites/player.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (375,386))
player_gravity = 0

# enemy
alien_surface = pygame.image.load('sprites/alien.png').convert_alpha()
alien_rect = alien_surface.get_rect(midbottom = (0,386))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player_rect.x += x_increment
    if keys[pygame.K_a]:
        player_rect.x -= x_increment
    if keys[pygame.K_SPACE] and player_rect.bottom >= 386:
        player_gravity = -11
        

    screen.fill((0,0,0))
    
    screen.blit(ground_surface,(0,386))


    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 386: player_rect.bottom = 386
    screen.blit(player_surface,player_rect)

    alien_rect.x += 4
    if alien_rect.x >= 800: alien_rect.x = 0
    screen.blit(alien_surface,alien_rect)

    if alien_rect.colliderect(player_rect):
        pygame.quit()
        exit

    pygame.display.update()
    clock.tick(60)