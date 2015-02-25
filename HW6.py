import pygame,sys
from random import randint
pygame.init()

def run_game():
    screenWidth = 640
    screenHeight = 480
    screen = pygame.display.set_mode((640,460),0,32)
    pygame.display.set_caption("Colliding!")

    background = pygame.Surface(screen.get_size())
    background.background.convert()
    background.fill((0,0,250))

    ##blue or black background image
    ##tardis is the one user controls

    enemy1=pygame.image.load("dalek.png").convert()
    enemy2=pygame.image.load("dalek.png").convert()
    enemy3=pygame.image.load("dalek.png").convert()
    
    clock=pygame.time.Clock()

    randomX = randint(0,screenWidth)
    randomY = randint(0,screenWidth)
    
    startX = 30
    startY = 30
    pathX=1
    pathY=1

    while True:
        clock.tick(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(background, (0,0))
        screen.blit(enemy1,(startX,startY))
        pygame.display.flip()

run_game()
