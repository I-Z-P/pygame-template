# platform template for pygame              ***ABOUT***
# authors: D1N3SHh                          ***AUTHORS***
# https://github.com/D1N3SHh/tetris         ***URL OF REPO***


import pygame
from pygame.math import Vector2


#####SETTINGS#####
HEIGHT = 1080
WIDTH = 1920
TICKRATE = 80
BLOCK_SIZE = 60
GRAVITY = 18
##################


class Level():
   def __init__(self, file):
       self.file = file
       self.blocks = [] # list of tills
       self.map = self.load_from_file()
       self.camera_position = Vector2(WIDTH / 2, 0)

   # loading map
   def load_from_file(self):
       map = []
       file = open(self.file + '.txt', 'r')
       data = file.read()
       file.close()
       data = data.split('\n')
       for x in data:
           map.append(list(x))
       return map

   def move_camera(self, player):
       self.camera_position.x += player.shift.x
   
   def render(self, screen):
       self.blocks = []
       y = 0
       for row in self.map:
           x = 0
           for block in row:
               if block != '0':
                   self.blocks.append(pygame.Rect(x * BLOCK_SIZE - self.camera_position.x, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                   if block == '1':
                       pygame.draw.rect(screen, (56,24,0), (x * BLOCK_SIZE - self.camera_position.x, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                   elif block == '2':
                       pygame.draw.rect(screen, (18,115,81), (x * BLOCK_SIZE - self.camera_position.x, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
               x += 1
           y += 1


class Player():
   def __init__(self, x, y, color):
       self.position = Vector2(x, y)
       self.shift = Vector2(0, 0)
       self.jump = Vector2(0, 0)
       self.color = color
       self.rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
       self.go_left = False
       self.go_right = False
       self.go_up = False
       self.collisions = {'left' : False, 'right' : False, 'top' : False, 'bottom' : False}

   # moving the player object
   def move(self, level):
       self.shift = Vector2(0, GRAVITY)
       self.position.y = int(self.position.y)

       # left / right section
       if self.go_left:
           self.go_left = False
           self.collisions = test_collisions(pygame.Rect(self.position.x - 1, self.position.y, BLOCK_SIZE, BLOCK_SIZE), level.blocks)
           if not self.collisions['left']:
               self.shift += Vector2(-10, 0)
       if self.go_right:
           self.go_right = False
           self.collisions = test_collisions(pygame.Rect(self.position.x + 1, self.position.y, BLOCK_SIZE, BLOCK_SIZE), level.blocks)
           if not self.collisions['right']:
               self.shift += Vector2(10, 0)

       # gravity section
       self.collisions = test_collisions(pygame.Rect(self.position.x, self.position.y + GRAVITY, BLOCK_SIZE, BLOCK_SIZE), level.blocks)
       if self.collisions['bottom']: 
           self.shift -= Vector2(0, GRAVITY)
           if self.position.y % BLOCK_SIZE > 0:
               self.position.y += BLOCK_SIZE - (self.position.y % BLOCK_SIZE)
           
       # jump section
       if self.go_up:
           self.go_up = False
           self.collisions = test_collisions(pygame.Rect(self.position.x, self.position.y + GRAVITY, BLOCK_SIZE, BLOCK_SIZE), level.blocks)
           if self.collisions['bottom']:
               self.jump = Vector2(0, -80)
       self.collisions = test_collisions(pygame.Rect(self.position.x, self.position.y - 1, BLOCK_SIZE, BLOCK_SIZE), level.blocks)
       if self.jump.y > GRAVITY or self.collisions['top']:
           self.jump = Vector2(0, 0)
       else: 
           self.jump *= 0.9
           self.shift += self.jump
           
       # new position
       self.position += self.shift
       self.position.x += ((WIDTH / 2) - self.position.x)
       self.rect = pygame.Rect(self.position.x, self.position.y, BLOCK_SIZE, BLOCK_SIZE)

   # checking if player is death
   def check_death(self):
       if self.position.y > HEIGHT:
           new_game()

   # render player
   def render(self, screen):
       pygame.draw.rect(screen, self.color, self.rect)


# render section
def render(screen, player, level):
   screen.fill((49, 113, 181))
   level.render(screen)
   player.render(screen)
   pygame.display.update()


# keyboard handling
def handle_events(player):
   for event in pygame.event.get():
       if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
           run = False
           pygame.quit()
   keys = pygame.key.get_pressed()
   if keys[pygame.K_a] or keys[pygame.K_LEFT]:
       player.go_left = True
   if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
       player.go_right = True
   if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]:
       player.go_up = True


# test direction of collison (rects have to overlap) 
def test_collisions(object, rects):
   collisions = {'left' : False, 'right' : False, 'top' : False, 'bottom' : False}
   for rect in rects:
       if object.colliderect(rect):
           if object.x <= rect.x:
               collisions['right'] = True
           if object.x >= rect.x:
               collisions['left'] = True
           if object.y >= rect.y:
               collisions['top'] = True
           if object.y <= rect.y:
               collisions['bottom'] = True
   return(collisions)


# game loop
def main_loop(run, screen, level, player):
   clock = pygame.time.Clock()
   while run:
       clock.tick(TICKRATE)
       handle_events(player)
       player.move(level)
       player.check_death()
       level.move_camera(player)
       render(screen, player, level)


# init new game
def new_game():
   run = True
   screen = pygame.display.set_mode((WIDTH, HEIGHT))
   level = Level('level_two')
   level.camera_position = Vector2(0, 0)
   player = Player(WIDTH / 2, 0, (255,255,0))
   main_loop(run, screen, level, player)


# launch new game on start
if __name__ == "__main__":
   new_game()