import pygame, sys

# initialize pygame
pygame.init()
clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.SysFont('', 35)

screen = pygame.display.set_mode((750, 450))
pygame.display.set_caption('Alien Dash')

def play():

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

  start_time = pygame.time.get_ticks()

  # TEXT
  textwhendeath_surface = font.render('you died, press ENTER to revive', False, (255, 255, 255))
  textwhendeath_rect = textwhendeath_surface.get_rect(center = (750/2,450/5))
  textscore_surface = font.render('score:', False, (255, 255, 255))
  textscore_rect = textscore_surface.get_rect(center = (750/2,450/2.3))

  while running:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False
    
      if not notdead:
        screen.blit(textwhendeath_surface,textwhendeath_rect)
        counting_text = font.render(str(counting_string), False, (255,255,255))
        counting_rect = counting_text.get_rect(center = (750/2,450/2))
        screen.blit(counting_text, counting_rect)
        screen.blit(textscore_surface, textscore_rect)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
          play()
        if keys[pygame.K_ESCAPE]:
          pygame.quit()
          exit()

      if notdead:
        counting_time = pygame.time.get_ticks() - start_time

        keys = pygame.key.get_pressed()

        counting_seconds = str((counting_time%100000)/1000).zfill(2)

        counting_string = "%s" % (counting_seconds)

        if keys[pygame.K_ESCAPE]:
          pygame.quit()
          exit()

        if keys[pygame.K_d]:
            player_rect.x += x_increment
        if keys[pygame.K_a]:
            player_rect.x -= x_increment
        if keys[pygame.K_SPACE] and player_rect.bottom >= 386:
            player_gravity = -11.1

        if keys[pygame.K_d] and player_rect.bottom >= 386 and keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            player_rect.x += x_increment/2
        if keys[pygame.K_a] and player_rect.bottom >= 386 and keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            player_rect.x -= x_increment/2
        if keys[pygame.K_SPACE] and keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            player_gravity = 0
        
        screen.fill((0,0,0))
    
        screen.blit(ground_surface,(0,386))

        counting_text = font.render(str(counting_string), 1, (255,255,255))
        counting_rect = counting_text.get_rect(topleft = screen.get_rect().topleft)

        screen.blit(counting_text, counting_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 386: player_rect.bottom = 386
        if player_rect.x >= 725: player_rect.x = 725
        if player_rect.x <= 0: player_rect.x = 0
        screen.blit(player_surface,player_rect)

        if counting_time >= 10000: alien_rect.x += 2
        if counting_time >= 20000: alien_rect.x += 3
        if counting_time >= 30000: alien_rect.x += 4
        if counting_time >= 40000: alien_rect.x += 5
        if counting_time >= 50000: alien_rect.x += 6

        alien_rect.x += 4
        if alien_rect.x >= 800: alien_rect.x = -100
        screen.blit(alien_surface,alien_rect)

      if alien_rect.colliderect(player_rect):
        notdead = False

      pygame.display.update()
      clock.tick(60)

play()