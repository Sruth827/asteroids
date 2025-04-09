import pygame
from circleshape import CircleShape
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Shot(CircleShape):
    def __init__(self, x, y, SHOT_RADIUS, image):
        super().__init__(x, y, SHOT_RADIUS)
        self.shot_img = image

    def draw(self, screen):
        rotation = self.velocity.angle_to(pygame.Vector2(0, -1))
        self.rotated_shot_img = pygame.transform.rotate(self.shot_img, rotation + 90)
        rect = self.rotated_shot_img.get_rect(center=self.position)
        screen.blit(self.rotated_shot_img, rect)


    def update(self, dt):
        self.position += (self.velocity * dt)

        # Destroy shot if it goes off-screen
        if self.position.x < 0 or self.position.x > SCREEN_WIDTH or \
           self.position.y < 0 or self.position.y > SCREEN_HEIGHT:
            self.kill()

