import sys
from random import randint, choice
from math import sin, cos, radians

import pygame
from pygame.sprite import Sprite
from pygame.locals import *

from vec2d import vec2d


class Creep(Sprite):
    
    def __init__(   
            self, screen, img_filename, init_position, 
            init_direction, speed):
        
        Sprite.__init__(self)
        
        self.screen = screen
        self.speed = speed
        
        self.base_image = pygame.image.load('dalek.png')
        self.image  = self.base_image
       
        self.pos = vec2d(init_position)

        self.direction = vec2d(init_direction).normalized()

        self.Rect = self.image.get_rect()
            
    def update(self, time_passed):
        
        displacement = vec2d(    
            self.direction.x * self.speed * time_passed,
            self.direction.y * self.speed)
        self.pos += displacement
        
        self.image_w, self.image_h = self.image.get_size()
        bounds_rect = self.screen.get_rect().inflate(
                        -self.image_w, -self.image_h)
        
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
        
        draw_pos = self.image.get_rect().move(
            self.pos.x - self.image_w / 2, 
            self.pos.y - self.image_h /2)
        self.screen.blit(self.image, draw_pos)

            
#----------------------- end of class ----------------------------------------------    

def run_game():
    screen_w, screen_h = 640, 480
    background = 0, 0, 150
    enemyPi = 'dalek.png'
    playerPic = pygame.image.load('tardis.png')
    

    #enemyHI = pygame.image.load('dalek.png')
    
    
    numOfDalek = 3
    collision_count = 0

    pygame.init()
    screen = pygame.display.set_mode(
                (screen_w, screen_h), 0, 32)
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("monospace",15)

    #start position for the player
    playerStartX = 260
    playerStartY = 300

    # Create N_CREEPS random creeps.
    dalek = []    
    for i in range(numOfDalek):
        dalek.append(Creep(screen,
                            enemyPi, 
                            (   randint(0, screen_w), 
                                randint(0, screen_h)), 
                            (   choice([-1, 1]), 
                                choice([0,0])),
                            0.2))
    #dalekBox = dalek.get_rect()
    
    while True:
        time_passed = clock.tick(50)
        label = font.render("Collisions: "+ str(collision_count),1,(255,255,0))
        label_pos = label.get_rect(centerx=screen.get_width()/2)
        #enemyPiBox = pygame.Rect(enemyHI.get_rect())
        #player1 = pygame.Rect(playerPic.get_rect())
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

        if(pygame.key.get_pressed()[pygame.K_UP] !=0):
            playerStartY -=5
            collision_count +=1
            label = font.render("Collisions: "+ str(collision_count),1,(255,255,0))
            
        if(pygame.key.get_pressed()[pygame.K_DOWN] !=0):
            playerStartY +=5
            collision_count -=1
            label = font.render("Collisions: "+ str(collision_count),1,(255,255,0))
            
        if(pygame.key.get_pressed()[pygame.K_LEFT] !=0):
            playerStartX -=5
            
        if(pygame.key.get_pressed()[pygame.K_RIGHT] !=0):
            playerStartX +=5

        if(pygame.key.get_pressed()[pygame.K_ESCAPE]):
            exit_game()

        
        screen.fill(background)
        #screen.blit(enemyHI, (200,50))
        screen.blit(playerPic, (playerStartX,playerStartY))
        screen.blit(label,label_pos)
        
        # Update the enemies
        for enemy in dalek:
            enemy.update(time_passed)
            enemy.blitme()

            '''if pygame.sprite.collide_rect(player1, enemy.Rect):
                collision_count +=1
'''
        pygame.display.flip()


def exit_game():
    sys.exit()


run_game()

