import pygame, sys

# initialize pygame
pygame.init()
clock = pygame.time.Clock()

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

screen = pygame.display.set_mode((750, 450))
pygame.display.set_caption('Alien Dash')

def play():
  
  # TEXT
  textwhendeath_surface = my_font.render('you died, press SPACE to revive', False, (255, 255, 255))
  textwhendeath_rect = textwhendeath_surface.get_rect(center = (750/2,450/3))
  
  # icon
  icon = pygame.image.load('sprites/ufo.png')
  icon_surface = pygame.display.set_icon(icon)

  # ground
  ground_surface = pygame.image.load('sprites/cobblestone.png').convert_alpha()

  # player
  x_increment = 4
  y_increment = 1
  player_surface = pygame.image.load('sprites/player.png').convert_alpha()
  player_rect = player_surface.get_rect(midbottom = (375,386))
  player_gravity = 0

  # enemy
  alien_surface = pygame.image.load('sprites/alien.png').convert_alpha()
  alien_rect = alien_surface.get_rect(midbottom = (0,386))
  
  running = True
  notdead = True


  while running:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False
    
      if not notdead:
        screen.blit(textwhendeath_surface,textwhendeath_rect)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
          play()
        if keys[pygame.K_ESCAPE]:
          pygame.quit()
          exit()

      if notdead:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
          pygame.quit()
          exit()

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
        if player_rect.x >= 725: player_rect.x = 725
        if player_rect.x <= 0: player_rect.x = 0
        screen.blit(player_surface,player_rect)

        alien_rect.x += 5
        if alien_rect.x >= 800: alien_rect.x = 0
        screen.blit(alien_surface,alien_rect)

      if alien_rect.colliderect(player_rect):
        notdead = False

      pygame.display.update()
      clock.tick(60)

play()