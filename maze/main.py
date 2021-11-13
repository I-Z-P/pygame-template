# maze template for pygame                  ***ABOUT***
# authors: D1N3SHh                          ***AUTHORS***
# https://github.com/D1N3SHh/tetris         ***URL OF REPO***


import pygame


#####SETTINGS#####
HEIGHT = 1080
WIDTH = 1920
BLOCK_SIZE = 60
##################


class Level():
    def __init__(self, file):
        self.file = file
        self.blocks = []
        self.map = self.load_from_file()

    def load_from_file(self):
        map = []
        file = open(self.file + '.txt', 'r')
        data = file.read()
        file.close()
        data = data.split('\n')
        for x in data:
            map.append(list(x))
        return map
     
    def render(self, screen):
        self.blocks = []
        y = 0
        for row in self.map:
            x = 0
            for block in row:
                if block != '0':
                    self.blocks.append(pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    if block == '1':
                        pygame.draw.rect(screen, (56,24,0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    elif block == '2':
                        pygame.draw.rect(screen, (18,115,81), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                x += 1
            y += 1


class Player():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
        self.go_left = False
        self.go_right = False
        self.go_up = False
        self.go_down = False
        self.collisions = {'left' : False, 'right' : False, 'top' : False, 'bottom' : False}

    def move(self):
        if self.go_left:
            self.go_left = False
            self.collisions = test_collisions(pygame.Rect(self.x - 1, self.y, BLOCK_SIZE, BLOCK_SIZE), level.blocks)
            if not self.collisions['left']: self.x -= 10
        if self.go_right:
            self.go_right = False
            self.collisions = test_collisions(pygame.Rect(self.x + 1, self.y, BLOCK_SIZE, BLOCK_SIZE), level.blocks)
            if not self.collisions['right']: self.x += 10
        if self.go_up:
            self.go_up = False
            self.collisions = test_collisions(pygame.Rect(self.x, self.y - 1, BLOCK_SIZE, BLOCK_SIZE), level.blocks)
            if not self.collisions['top']: self.y -= 10
        if self.go_down: 
            self.go_down = False
            self.collisions = test_collisions(pygame.Rect(self.x, self.y + 1, BLOCK_SIZE, BLOCK_SIZE), level.blocks)
            if not self.collisions['bottom']: self.y += 10
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


def render(screen, player, level):
    screen.fill((49, 113, 181))
    level.render(screen)
    player.render(screen)
    pygame.display.update()


def handle_events(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.go_left = True
    if keys[pygame.K_d]:
        player.go_right = True
    if keys[pygame.K_w]:
        player.go_up = True
    if keys[pygame.K_s]:
        player.go_down = True


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

    
def main_loop():
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        handle_events(player)
        player.move()
        render(screen, player, level)


if __name__ == "__main__":
    run = True
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    level = Level('maze')
    player = Player(60,60,(255,255,0))
    main_loop()