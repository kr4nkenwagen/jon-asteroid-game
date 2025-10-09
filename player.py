from constants import PLAYER_ACCELERATION, PLAYER_DEACCELERATION, PLAYER_MAX_SPEED, PLAYER_RADIUS,PLAYER_TURN_SPEED
from entity import entity
from player_polygon import player_polygon
from player_thrust_polygon import player_thrust_polygon
import pygame

class player(entity):
    
    def __init__(self, x, y):
        self.polygon = player_polygon()
        super().__init__(x, y, PLAYER_RADIUS)

    def forward(self):
        return pygame.Vector2(0, 1).rotate(self.rotation)
    
    def rotate(self, dt, keys):
        direction = 0;
        if keys[pygame.K_a]:
            direction += 1
        if keys[pygame.K_d]:
            direction -= 1
        self.rotation += direction * PLAYER_TURN_SPEED * dt

    def accelerate(self, dt):
        self.velocity = self.velocity.lerp(self.forward() * PLAYER_MAX_SPEED, PLAYER_ACCELERATION / PLAYER_MAX_SPEED * dt)

    def deaccelerate(self, dt):
        self.velocity = self.velocity.lerp(pygame.Vector2(0, 0), PLAYER_ACCELERATION / PLAYER_MAX_SPEED * dt)

    def move(self, dt, keys):
        if keys[pygame.K_w]:
            self.accelerate(dt)
        else:
            self.deaccelerate(dt)
        self.position += self.velocity * dt

    def update(self):
        keys = pygame.key.get_pressed()
        self.rotate(self.game.dt, keys)
        self.move(self.game.dt, keys)
