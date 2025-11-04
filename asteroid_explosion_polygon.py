from constants import ASTEROID_EXPLOSION_RADIUS, ASTEROID_EXPLOSION_EXPAND_RATE, ASTEROID_EXPLOSION_MAX_JITTER, ASTEROID_EXPLOSION_LIFETIME, ASTEROID_EXPLOSION_THICKNESS, ASTEROID_EXPLOSION_COLOR, ASTEROID_EXPLOSION_MAX_NUM_POINTS, ASTEROID_EXPLOSION_MIN_NUM_POINTS
import polygon
import pygame
import random
from polygon import polygon


class asteroid_explosion_polygon(polygon):
    def __init__(self):
        super().__init__()
        self.timer = 0
        self.expand_rate = ASTEROID_EXPLOSION_EXPAND_RATE
        self.max_jitter = ASTEROID_EXPLOSION_MAX_JITTER
        self.color = ASTEROID_EXPLOSION_COLOR
        self.thickness = ASTEROID_EXPLOSION_THICKNESS
        self.points = []
        self.base_shape = []
        num_points = random.randint(
            ASTEROID_EXPLOSION_MIN_NUM_POINTS, ASTEROID_EXPLOSION_MAX_NUM_POINTS)
        for i in range(num_points):
            angle = (360 / num_points) * i
            jitter = random.uniform(-self.max_jitter, self.max_jitter)
            # store base angle & offset scale
            self.base_shape.append((angle, 1 + jitter * 0.05))

    def calc(self, position, rotation, radius, dt):
        self.timer += dt
        expand = 1 + self.timer * self.expand_rate / 100
        self.points = []
        for angle, scale in self.base_shape:
            dist = ASTEROID_EXPLOSION_RADIUS * scale * expand
            offset = pygame.Vector2(0, -dist).rotate(angle + rotation)
            self.points.append(position + offset)
