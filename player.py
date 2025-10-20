from constants import PLAYER_ACCELERATION, PLAYER_DEACCELERATION, PLAYER_MAX_SPEED, PLAYER_RADIUS,PLAYER_TURN_SPEED
from entity import entity
from player_polygon import player_polygon
from player_thrust_polygon import player_thrust_polygon
from player_thurst_representation import player_thrust_representation
import pygame

class player(entity):
    thrust_representation = None

    def __init__(self, x, y):
        self.polygon = player_polygon()
        self.collideable = True
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
        self.thrust_representation.show = True
        self.velocity = self.velocity.lerp(self.forward() * PLAYER_MAX_SPEED, PLAYER_ACCELERATION / PLAYER_MAX_SPEED * dt)

    def deaccelerate(self, dt):
        self.thrust_representation.show = False
        self.velocity = self.velocity.lerp(pygame.Vector2(0, 0), PLAYER_DEACCELERATION / PLAYER_MAX_SPEED * dt)

    def move(self, dt, keys):
        if keys[pygame.K_w]:
            self.accelerate(dt)
        else:
            self.deaccelerate(dt)
        #self.position += self.velocity * dt

    def update(self):
        if self.thrust_representation == None:
            self.thrust_representation = self.game.ent_manager.add_entity(player_thrust_representation(self.position.x, self.position.y, 10))
            self.thrust_representation.parent = self
        keys = pygame.key.get_pressed()
        self.rotate(self.game.dt, keys)
        self.move(self.game.dt, keys)

    def on_collision(self, entity):
        print("Player collided with " + str(entity.id))
        self.velocity += entity.velocity / 100
