import pygame
import random
from constants import *
from circleshape import CircleShape
import random
class Asteroid(CircleShape):
    #sprite_group = None  
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius,2)
    def update(self, dt):
        self.position+=self.velocity*dt
    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        random_angle=random.uniform(20,50)
        velocity1 = self.velocity.rotate(random_angle) * 1.2 # Rotate velocity by +random_angle
        velocity2 = self.velocity.rotate(-random_angle) * 1.2 # Rotate velocity by -random_angle

        new_asteroid1 = Asteroid(self.position.x, self.position.y,self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)

        new_asteroid1.velocity = velocity1
        new_asteroid2.velocity = velocity2
        # Asteroid.sprite_group.add(new_asteroid1)
        # Asteroid.sprite_group.add(new_asteroid2)





    