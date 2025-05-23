import pygame 

#Base class for game obj
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        #will use later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
            #subclasses must override
            pass

    def update(self, dt):
           #subclasses must override
           pass


    def collision_check(self, CircleShape):
        distance = self.position.distance_to(CircleShape.position)
        return distance < (self.radius + CircleShape.radius)
