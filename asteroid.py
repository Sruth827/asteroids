import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        asteroid_image = pygame.image.load("asteroid_transparent.png").convert_alpha()
        scaled_asteroid_image = pygame.transform.scale(asteroid_image, (self.radius * 2 , self.radius * 2))
        rect = scaled_asteroid_image.get_rect(center=self.position)
        screen.blit(scaled_asteroid_image, rect )
        
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
         
        random_angle = random.uniform(20, 50)
        vec1 = self.velocity.rotate(random_angle)
        vec2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_1 = Asteroid(self.position.x, self.position.y, new_radius)
        split_1.velocity = vec1 * 1.2
        split_2 = Asteroid(self.position.x, self.position.y, new_radius)
        split_2.velocity = vec2 * 1.2
        
        
