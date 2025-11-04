from constants import LASER_COLOR
import pygame
from polygon import polygon


class player_shot_polygon(polygon):
    def __init__(self):
        super().__init__()
        self.length = 0

    def calc(self, position, rotation, radius, dt):
        half_length = self.length / 2
        self.points = [
            pygame.Vector2(0, -half_length),
            pygame.Vector2(1, -half_length),
            pygame.Vector2(1, half_length),
            pygame.Vector2(0, half_length)
        ]
        self.points = [position + p.rotate(rotation) for p in self.points]
        self.color = LASER_COLOR
