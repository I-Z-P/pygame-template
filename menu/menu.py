# endless runner, nuke themed game
# authors: D1N3SHh, Naris404, dzidek
# https://github.com/I-Z-P/nuke_racer


import pygame
from pygame.constants import MOUSEBUTTONDOWN
pygame.init()


#####SETTINGS#####
HEIGHT = 1080
WIDTH = 1920
##################


class Menu():
    def __init__(self):
        self.run = True
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.font = pygame.font.SysFont('arial', 200)
        self.start_button = pygame.Rect(WIDTH / 4, HEIGHT / 2 - 100, WIDTH / 2, 200)
        self.start_button_collor = (111, 111, 111)
        self.start_button_text = self.font.render('Start', True, (0, 0, 0))

    # rendering menu
    def render(self):
        self.screen.fill((49, 113, 181))
        pygame.draw.rect(self.screen, self.start_button_collor, self.start_button)
        self.screen.blit(self.start_button_text, (WIDTH / 2 - 225, HEIGHT / 2 - 100))
        pygame.display.update()

    # looping and handling menu
    def loop(self):
        while self.run:
            mouse = pygame.mouse.get_pos()
            if WIDTH - WIDTH / 4 >= mouse[0] >= WIDTH / 4 and HEIGHT / 2 + 100 >= mouse[1] >= HEIGHT /2 - 100:
                self.start_button_collor = (50, 50, 50)
            else: self.start_button_collor = (111, 111, 111)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.run = False
                    pygame.quit()
                if event.type == MOUSEBUTTONDOWN:
                    if WIDTH - WIDTH / 4 >= mouse[0] >= WIDTH / 4 and HEIGHT / 2 + 100 >= mouse[1] >= HEIGHT /2 - 100:
                        self.run = False
                        new_game()  # function that run on click
            self.render()


# launch menu on start
if __name__ == "__main__":
    menu = Menu()
    menu.loop()