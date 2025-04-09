import sys
import pygame
from pygame.sprite import Group
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main(): 
    #initialize
    pygame.init()
    #create clock so fps can be capped
    clock = pygame.time.Clock()
    
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #background image 
    bg_image = pygame.image.load('space.jpg')
    bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    asteroid_image = pygame.image.load("asteroid_transparent.png").convert_alpha()
    
    #groups to be used as containers
    updatable = Group()
    drawable = Group()
    asteroids = Group()
    shots_group = Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots_group, updatable, drawable)
    
    player = Player(x, y, PLAYER_RADIUS)
    player.shots_group = shots_group
    asteroidfield = AsteroidField(asteroid_image)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #fill screen with color black
        screen.blit(bg_image, (0, 0))
        
        #draw player 
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game over!")
                pygame.quit()
                sys.exit()
        for asteroid in asteroids:
            for shot in shots_group:
                if asteroid.collision_check(shot):
                    asteroid.split()
                    shot.kill()

        for drawings in drawable:
            drawings.draw(screen)
        #flip display
        pygame.display.flip()
        #maintain 60fps
        dt = clock.tick(144) / 1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    

if __name__ == "__main__":
        main()


