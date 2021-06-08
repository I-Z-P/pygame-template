# simple 101 template for pygame            ***ABOUT***
# authors: D1N3SHh                          ***AUTHORS***
# https://github.com/D1N3SHh/tetris         ***URL OF REPO***


import pygame


class Player():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = (x, y, 10, 10)


    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.x -= 10
        elif keys[pygame.K_d]:
            self.x += 10
        elif keys[pygame.K_w]:
            self.y -= 10
        elif keys[pygame.K_s]:
            self.y += 10

        self.rect = (self.x, self.y, 10, 10)


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


def drawing(screen, player):
    screen.fill((0,0,0))
    player.draw(screen)
    pygame.display.update()


def main():
    run = True
    screen = pygame.display.set_mode((1000, 1000))
    clock = pygame.time.Clock()
    player = Player(0,0,(0,255,0))

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()

        player.move()
        drawing(screen, player)


if __name__ == "__main__":
    main()