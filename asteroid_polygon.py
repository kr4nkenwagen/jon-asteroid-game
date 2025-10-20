from random import randint
from polygon import polygon
import pygame

class asteroid_polygon(polygon):
    asteroid_shapes = [

        # Asteroid 1 – Irregular pentagon
        [
            pygame.Vector2(0.8, 0),
            pygame.Vector2(0.4, 0.6),
            pygame.Vector2(-0.2, 0.8),
            pygame.Vector2(-0.9, 0.3),
            pygame.Vector2(-0.6, -0.7),
            pygame.Vector2(0.1, -0.9),
        ],

        # Asteroid 2 – More compact with bulges
        [
            pygame.Vector2(0.9, -0.1),
            pygame.Vector2(0.5, 0.5),
            pygame.Vector2(0.2, 0.9),
            pygame.Vector2(-0.4, 0.6),
            pygame.Vector2(-0.7, 0.2),
            pygame.Vector2(-0.6, -0.4),
            pygame.Vector2(-0.1, -0.8),
            pygame.Vector2(0.4, -0.6),
        ],

        # Asteroid 3 – Elongated, pointy
        [
            pygame.Vector2(1.0, 0.0),
            pygame.Vector2(0.6, 0.7),
            pygame.Vector2(0.0, 1.0),
            pygame.Vector2(-0.5, 0.8),
            pygame.Vector2(-1.0, 0.1),
            pygame.Vector2(-0.6, -0.6),
            pygame.Vector2(0.0, -1.0),
            pygame.Vector2(0.7, -0.5),
        ],

        # Asteroid 4 – Symmetrical but lumpy
        [
            pygame.Vector2(0.7, -0.2),
            pygame.Vector2(1.0, 0.2),
            pygame.Vector2(0.6, 0.7),
            pygame.Vector2(0.0, 1.0),
            pygame.Vector2(-0.6, 0.7),
            pygame.Vector2(-1.0, 0.0),
            pygame.Vector2(-0.5, -0.7),
            pygame.Vector2(0.0, -1.0),
        ],

        # Asteroid 5 – Chaotic and jagged
        [
            pygame.Vector2(0.8, 0.1),
            pygame.Vector2(0.5, 0.9),
            pygame.Vector2(-0.2, 0.7),
            pygame.Vector2(-0.9, 0.2),
            pygame.Vector2(-0.5, -0.3),
            pygame.Vector2(-0.7, -0.8),
            pygame.Vector2(0.1, -0.6),
            pygame.Vector2(0.6, -0.4),
        ],
    ]

    shape_index = 0

    def __init__(self):
        super().__init__()
        self.shape_index = randint(0, len(self.asteroid_shapes) -1)

    def calc(self, position, rotation, radius):
        shape = self.asteroid_shapes[self.shape_index]
        self.points = [ (point.rotate(rotation) * radius + position) for point in shape ]
