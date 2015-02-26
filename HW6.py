import pygame, sys
from pygame.sprite import Sprite
from random import randint,choice

from vec2d import vec2d


class Enemy(Sprite):
    def __init__(
        self, screen, enemyImg, startPosition, direction, speed):
        Sprite.__init__(self)

        self.screen = screen
        self.speed = speed

        self.base_image = pygame.image.load("dalek.png").convert_alpha()
        self.image = self.base_image

        self.pos = vec2d(startPosition)

        self.direction = vec2d(direction).normalized()

    def update(self, timePassed):
        self._change_direction(timePassed)

        self.image = pygame.transform.rotate(self.base_image, -self.direction.angle)

        displacement = vec2d(self.direction.x * self.speed * timePassed,
                             self.direction.y * self.speed * timePassed)
        self.pos += displacement

        self.image_w, self.image_h, self.image.get_size()
        bounds_rect = self.screen.get_rect().inflate(-self.image_w, -self.image_h)

        if self.pos.x < bounds_rect.left:
            self.pos.x = bounds_rect.left
            self.direction.x *= -1
        elif self.pos.x > bounds_rect.right:
            self.pos.x = bounds_rect.right
            self.direction.x *= -1
        elif self.pos.y < bounds_rect.top:
            self.pos.y = bounds_rect.top
            self.direction.y *= -1
        elif self.pos.y > bounds_rect.bottom:
            self.pos.y = bounds_rect.bottom
            self.direction.y *= -1

    def blitme(self):
        draw_pos = self.image.get_rect().move(self.pos.x - self.image_w/2,
                                              self.pos.y - self.image_h/2)
        self.screen.blit(self.image, draw_pos)

    _count = 0

    def _change_direction(self, timePassed):
        self._count += timePassed
        if self._count > randint(300,600):
            self.direction.rotate(60 * randint(-1,1))


def run_game():
    
    pygame.display.set_caption("Assignment 5")
    background_color = 0, 0, 100
    enemyNum = 3
    enemyPic = 'dalek.png'
    pygame.init()

    screen = pygame.display.set_mode((600,480))
   
    clock = pygame.time.Clock()

    enemies = []
    for i in range(enemyNum):
        enemies.append(Enemy(screen, enemyPic,
                             (randint(0,600),
                              randint(0,480)),
                             (choice([-1,1]),
                              choice([-1,1])),
                             0.5))

    while True:
        timePassed = clock.tick(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(background_color)

        for enemy in enemies:
            enemy.update(timePassed)
            enemy.blitme()
        
        pygame.display.flip()

def exitGame():
    sys.exit()
    

run_game()
