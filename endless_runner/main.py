# platform template for pygame              ***ABOUT***
# authors: D1N3SHh                          ***AUTHORS***
# https://github.com/D1N3SHh/tetris         ***URL OF REPO***


import pygame
from level import *
from player import *
from config import *


# keyboard handling
def handle_events(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
            pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            player.jump = True


# game loop
def main_loop(run, screen, player, level, camera):
    clock = pygame.time.Clock()
    while run:
        clock.tick(TICKRATE)
        screen.fill((49, 113, 181))
        handle_events(player)
        player.check_ground(level.ground)
        player.move()
        player.render(screen)
        camera.follow_player(player)
        level.render(screen, camera)
        pygame.display.update()


# init new game
def new_game():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    player = Player()
    camera = Camera()
    level = Level()
    main_loop(True, screen, player, level, camera)


# launch new game on start
if __name__ == "__main__":
    new_game()