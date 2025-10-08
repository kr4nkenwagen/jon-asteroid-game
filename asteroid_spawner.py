from asteroid import asteroid
import pygame
import random
from constants import ASTEROID_MAX_RADIUS, ASTEROID_MAX_SPEED, ASTEROID_MIN_RADIUS, ASTEROID_MIN_SPEED, ASTEROID_SPAWN_RATE, SCREEN_HEIGHT, SCREEN_WIDTH
from entity import entity


class asteroid_spawner(entity):
    timer = 0 
    player = None

    def __init__(self):
        super().__init__(0, 0, 0)

    def update(self):
        if self.player == None:
            self.player = self.game.ent_manager.get_entity("player")
        if self.timer >= ASTEROID_SPAWN_RATE:
            self.timer = 0
            self.spawn_asteroid()
        self.timer += self.game.dt

    def spawn_asteroid(self):
        position = self.create_asteroid_position()
        asteroid_ent = self.game.ent_manager.add_entity(asteroid(position.x, position.y, 30))
        asteroid_ent.velocity = self.create_asteroid_velocity(position)
        asteroid_ent.radius = self.create_asteroid_radius()

    def create_asteroid_position(self):
        edge = random.randint(0, 3)
        position = pygame.Vector2(0, 0)
        if edge == 0:
            position.y = random.randint(0, SCREEN_HEIGHT)
        if edge == 1:
            position.x = random.randint(0, SCREEN_WIDTH)
        if edge == 2:
            position.x = SCREEN_WIDTH
            position.y = random.randint(0, SCREEN_HEIGHT)
        if edge == 3:
            position.x = random.randint(0, SCREEN_WIDTH)
            position.y = SCREEN_HEIGHT
        return position

    def create_asteroid_velocity(self, start):
        if self.player == None:
            return (pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)- start) * random.randint(ASTEROID_MIN_SPEED, ASTEROID_MAX_SPEED)* self.game.dt
        return (self.player.position - start) * random.randint(ASTEROID_MIN_SPEED, ASTEROID_MAX_SPEED)* self.game.dt

    def create_asteroid_radius(self):
        return random.randint(ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS)

