import pygame

pygame.init()

width, height = 750, 450
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Alien Dash')
clock = pygame.time.Clock()

# ufo icon
icon_surface = pygame.image.load('sprites/ufo.png')
icon = pygame.display.set_icon(icon_surface)

# music
alien_anthem = pygame.mixer.music.load('game_song.wav')
pygame.mixer.music.play('alien_anthem')

# player
player_x = 0
player_y = 0
x_increment = 2
y_increment = 1
player_surface = pygame.image.load('sprites/player.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (200,350))
player_gravity = 0
on_ground = True

# background
background_surface = pygame.image.load('sprites/background.png').convert()
background_rect = background_surface.get_rect(center = (750/2, 450/2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player_rect.x = player_rect.x + x_increment
    if keys[pygame.K_a]:
        player_rect.x = player_rect.x - x_increment
    if keys[pygame.K_SPACE] and player_rect.bottom >= 400:
        if on_ground:
            player_gravity = -17
            

    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 400: player_rect.bottom = 400
    screen.blit(background_surface,background_rect)
    screen.blit(player_surface,player_rect)
    pygame.display.update()
    clock.tick(60)
