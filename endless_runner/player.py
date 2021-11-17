# platform template for pygame              ***ABOUT***
# authors: D1N3SHh                          ***AUTHORS***
# https://github.com/D1N3SHh/tetris         ***URL OF REPO***


import pygame
from pygame.math import Vector2
from config import *
from main import *


class Player():
    def __init__(self):
        self.position = Vector2(WIDTH / 4, 0)
        self.velocity = Vector2(10, 0)
        self.acceleration = Vector2(0.005, GRAVITY)
        # self.model = pygame.image.load('assets/player_model.png')     # uncomment to load player assets
        self.rect = pygame.Rect(self.position.x, self.position.y, BLOCK_SIZE, BLOCK_SIZE * 2)
        self.jump = False

    # checking if player is on ground and if so, it disables gravity
    def check_ground(self, ground):
        self.acceleration.y = GRAVITY
        for tile in ground:
            if self.rect.colliderect(tile):
                self.position.y = tile.top - BLOCK_SIZE * 2 + 1
                self.acceleration.y *= 0
                self.velocity.y *= 0
                self.on_ground = True

    # player movement
    def move(self):
        if self.jump and self.on_ground:
            self.velocity.y -= 25
            self.acceleration.y = 1
        self.jump = False
        self.on_ground = False
        self.velocity += self.acceleration
        self.position += self.velocity
        self.position.x += ((WIDTH / 4) - self.position.x) # stick player to 1/4 of screen
        self.rect = pygame.Rect(self.position.x, self.position.y, BLOCK_SIZE, BLOCK_SIZE * 2)

    # rendering player
    def render(self, screen):
        # screen.blit(self.model, self.rect)                        # if you are using player assets, uncomment this line
        pygame.draw.rect(screen, (100, 100, 100), self.rect)        # and comment this line


# launch new game on start
if __name__ == "__main__":
    new_game()