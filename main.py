# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import *
from AsteroidField import *
from shot import Shot
def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    dt=0
    clock=pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    shots=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()

    Asteroid.containers=(asteroids,updatable,drawable)
    AsteroidField.containers=updatable
    asteroid_field=AsteroidField()

    Player.containers = (updatable, drawable)
    Shot.containers=(shots,updatable,drawable)
    player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #player.update(dt)
        for sprite in updatable:
            sprite.update(dt)
            
        
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        #player.draw(screen)
        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        for object in asteroids:
            if object.collision(player):
                print("Game Over!")
                
        for shot in shots:
            for asteroid in asteroids:
                if asteroid.collision(shot):
                    shot.kill()  # Remove the shot from all groups
                    asteroid.split()  # Remove the asteroid from all groups
                    print("Shot destroyed an asteroid!")


            
            
       
        
        
if __name__ == "__main__":
    main()