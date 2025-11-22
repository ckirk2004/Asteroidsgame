import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

pygame.init()
pygame.display.set_caption("Asteroids")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Framerate variables
clock = pygame.time.Clock()
#delta
dt = 0

#groups
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

#containers for groups
Player.containers = (drawable, updatable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)


#instantiate player object
player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

#instantiate AsteroidField
asteroid_field = AsteroidField()

while True:
    log_state()
    #close window event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    dt = (clock.tick(60)) / 1000
    
    #set canvas to black
    screen.fill('black')

    #render player
    updatable.update(dt)

    for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game Over")
                quit()

    for obj in drawable:
        obj.draw(screen)
    

    #end of frames
    pygame.display.flip()
    #print(dt)

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print("Screen width: 1280")
    print("Screen height: 720")


if __name__ == "__main__":
    main()
