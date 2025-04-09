import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOT_SPEED, PLAYER_SHOOT_COOLDOWN
from circleshape import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, PLAYER_RADIUS, craft, image):
        super().__init__(x, y, PLAYER_RADIUS)       
        self.rotation = 0
        self.timer = 0
        self.craft_image = craft
        self.scaled_craft_image = pygame.transform.scale(self.craft_image, (self.radius *3, self.radius *3))
        self.shot_img = image
        self.scaled_shot_img = pygame.transform.scale(self.shot_img, (self.radius * 1.5 , self.radius * 1)) 
        self.rotated_shot_img = pygame.transform.rotate(self.scaled_shot_img, -self.rotation + 90)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius 
        b = self.position - forward * self.radius - right 
        c = self.position - forward * self.radius + right 
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255, 1), self.position, self.radius, 2)
        self.rotated_craft_image = pygame.transform.rotate(self.scaled_craft_image, -self.rotation + 270)
        rect = self.rotated_craft_image.get_rect(center=self.position)
        screen.blit(self.rotated_craft_image, rect)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-1 * dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_s]:
            self.move(dt)
        if keys[pygame.K_SPACE]: 
            if self.timer > 0:
                pass
            else: 
                self.shoot(dt)
        


    def shoot(self, dt):
        self.timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y , SHOT_RADIUS, self.scaled_shot_img)
        velocity = pygame.Vector2(0, 1).rotate(self.rotation)* PLAYER_SHOT_SPEED
        shot.velocity = velocity

        self.shots_group.add(shot)


