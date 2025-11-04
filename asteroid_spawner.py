from asteroid import asteroid
import math
import pygame
import random
from constants import ASTEROID_MAX_RADIUS, \
    ASTEROID_MAX_SPEED, \
    ASTEROID_MIN_RADIUS, \
    ASTEROID_MIN_SPEED, \
    ASTEROID_SPAWN_RATE, \
    SCREEN_HEIGHT, \
    SCREEN_WIDTH
from entity import entity


class asteroid_spawner(entity):
    timer = 0
    player = None

    def __init__(self):
        super().__init__(0, 0, 0)

    def update(self):
        if not self.player:
            self.player = self.game.ent_manager.get_entity("player")
        if self.timer >= ASTEROID_SPAWN_RATE:
            self.timer = 0
            self.spawn_asteroid()
        self.timer += self.game.dt

    def spawn_asteroid(self):
        if not self.player:
            return
        position = self.create_asteroid_position()
        asteroid_ent = self.game.ent_manager.add_entity(
            asteroid(position.x, position.y, self.create_asteroid_radius()))
        asteroid_ent.velocity = self.create_asteroid_velocity(position)
        asteroid_ent.radius = self.create_asteroid_radius()

    def create_asteroid_position(self):
        player_pos = self.player.position
        player_vel = self.player.velocity
        if player_vel.length() > 0:
            player_dir = player_vel.normalize()
            max_angle_offset = math.radians(60)  # 60° cone
            angle_offset = random.uniform(-max_angle_offset, max_angle_offset)
            spawn_dir = player_dir.rotate_rad(angle_offset)
            distance = max(SCREEN_WIDTH, SCREEN_HEIGHT) * 0.6
            position = player_pos + spawn_dir * distance
            position.x = max(0, min(position.x, SCREEN_WIDTH))
            position.y = max(0, min(position.y, SCREEN_HEIGHT))
            return position
        else:
            edge = random.choice(["top", "bottom", "left", "right"])
            position = pygame.Vector2(0, 0)
            if edge == "top":
                position.x = random.randint(0, SCREEN_WIDTH)
            if edge == "bottom":
                position.x = random.randint(0, SCREEN_WIDTH)
                position.y = SCREEN_HEIGHT
            if edge == "left":
                position.y = random.randint(0, SCREEN_HEIGHT)
            if edge == "right":
                position.x = SCREEN_WIDTH
                position.x = random.randint(0, SCREEN_HEIGHT)
            return position

    def create_asteroid_velocity(self, start):
        if not self.player:
            return (pygame.Vector2(SCREEN_WIDTH // 2,
                                   SCREEN_HEIGHT // 2) - start).normalize() * \
                random.randint(ASTEROID_MIN_SPEED, ASTEROID_MAX_SPEED)
        return (self.player.position - start).normalize() * \
            random.randint(ASTEROID_MIN_SPEED, ASTEROID_MAX_SPEED)

    def create_asteroid_radius(self):
        return random.randint(ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS)
