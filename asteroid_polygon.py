from random import randint
from constants import ASTEROID_COLOR, ASTEROID_THICKNESS
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

        # Asteroid 6 – Smooth hexagon
        [
            pygame.Vector2(0.9, 0.0),
            pygame.Vector2(0.45, 0.8),
            pygame.Vector2(-0.45, 0.8),
            pygame.Vector2(-0.9, 0.0),
            pygame.Vector2(-0.45, -0.8),
            pygame.Vector2(0.45, -0.8),
        ],

        # Asteroid 7 – Squashed oval
        [
            pygame.Vector2(1.0, 0.0),
            pygame.Vector2(0.7, 0.6),
            pygame.Vector2(0.0, 0.8),
            pygame.Vector2(-0.7, 0.6),
            pygame.Vector2(-1.0, 0.0),
            pygame.Vector2(-0.8, -0.5),
            pygame.Vector2(0.0, -0.7),
            pygame.Vector2(0.8, -0.5),
        ],

        # Asteroid 8 – Cratered look
        [
            pygame.Vector2(0.9, 0.0),
            pygame.Vector2(0.6, 0.4),
            pygame.Vector2(0.2, 0.8),
            pygame.Vector2(-0.4, 0.9),
            pygame.Vector2(-0.8, 0.2),
            pygame.Vector2(-0.6, -0.6),
            pygame.Vector2(0.0, -1.0),
            pygame.Vector2(0.7, -0.4),
        ],

        # Asteroid 9 – Shattered rock
        [
            pygame.Vector2(1.0, 0.1),
            pygame.Vector2(0.6, 0.8),
            pygame.Vector2(0.1, 1.0),
            pygame.Vector2(-0.5, 0.7),
            pygame.Vector2(-0.9, 0.0),
            pygame.Vector2(-0.7, -0.6),
            pygame.Vector2(-0.2, -1.0),
            pygame.Vector2(0.4, -0.8),
            pygame.Vector2(0.8, -0.3),
        ],

        # Asteroid 10 – Chunky and asymmetrical
        [
            pygame.Vector2(0.9, -0.3),
            pygame.Vector2(0.7, 0.6),
            pygame.Vector2(0.0, 1.0),
            pygame.Vector2(-0.6, 0.7),
            pygame.Vector2(-0.9, -0.1),
            pygame.Vector2(-0.5, -0.8),
            pygame.Vector2(0.3, -0.9),
            pygame.Vector2(0.9, -0.5),
        ],

        # Asteroid 11 – Compact and rocky
        [
            pygame.Vector2(0.8, 0.2),
            pygame.Vector2(0.5, 0.7),
            pygame.Vector2(-0.2, 0.8),
            pygame.Vector2(-0.8, 0.4),
            pygame.Vector2(-0.7, -0.3),
            pygame.Vector2(-0.2, -0.9),
            pygame.Vector2(0.4, -0.7),
            pygame.Vector2(0.9, -0.2),
        ],

        # Asteroid 12 – Tri-lobed
        [
            pygame.Vector2(1.0, 0.0),
            pygame.Vector2(0.0, 1.0),
            pygame.Vector2(-1.0, 0.0),
            pygame.Vector2(0.0, -0.8),
        ],

        # Asteroid 13 – Fragmented ring
        [
            pygame.Vector2(0.9, 0.1),
            pygame.Vector2(0.6, 0.7),
            pygame.Vector2(-0.2, 0.9),
            pygame.Vector2(-0.9, 0.3),
            pygame.Vector2(-0.8, -0.4),
            pygame.Vector2(-0.3, -0.9),
            pygame.Vector2(0.5, -0.8),
            pygame.Vector2(0.9, -0.3),
        ],

        # Asteroid 14 – Very elongated
        [
            pygame.Vector2(1.0, 0.0),
            pygame.Vector2(0.8, 0.3),
            pygame.Vector2(0.3, 0.6),
            pygame.Vector2(-0.3, 0.5),
            pygame.Vector2(-1.0, 0.0),
            pygame.Vector2(-0.5, -0.4),
            pygame.Vector2(0.4, -0.5),
            pygame.Vector2(0.9, -0.2),
        ],

        # Asteroid 15 – Chunky triangle
        [
            pygame.Vector2(0.9, -0.2),
            pygame.Vector2(0.2, 0.9),
            pygame.Vector2(-0.8, 0.5),
            pygame.Vector2(-0.9, -0.3),
            pygame.Vector2(-0.1, -0.9),
            pygame.Vector2(0.7, -0.7),
        ],

        # Asteroid 16 – Compact lump
        [
            pygame.Vector2(0.7, 0.0),
            pygame.Vector2(0.5, 0.5),
            pygame.Vector2(-0.2, 0.8),
            pygame.Vector2(-0.7, 0.3),
            pygame.Vector2(-0.8, -0.3),
            pygame.Vector2(-0.2, -0.7),
            pygame.Vector2(0.3, -0.8),
            pygame.Vector2(0.8, -0.3),
        ],

        # Asteroid 17 – Jagged crystal
        [
            pygame.Vector2(1.0, 0.0),
            pygame.Vector2(0.7, 0.6),
            pygame.Vector2(0.0, 0.9),
            pygame.Vector2(-0.6, 0.5),
            pygame.Vector2(-0.9, -0.1),
            pygame.Vector2(-0.6, -0.7),
            pygame.Vector2(0.0, -1.0),
            pygame.Vector2(0.6, -0.8),
        ],

        # Asteroid 18 – Flattened slab
        [
            pygame.Vector2(1.0, 0.0),
            pygame.Vector2(0.8, 0.3),
            pygame.Vector2(0.2, 0.5),
            pygame.Vector2(-0.2, 0.5),
            pygame.Vector2(-0.8, 0.3),
            pygame.Vector2(-1.0, 0.0),
            pygame.Vector2(-0.8, -0.3),
            pygame.Vector2(-0.2, -0.5),
            pygame.Vector2(0.8, -0.3),
        ],

        # Asteroid 19 – Highly irregular
        [
            pygame.Vector2(0.9, 0.1),
            pygame.Vector2(0.6, 0.8),
            pygame.Vector2(0.0, 0.9),
            pygame.Vector2(-0.7, 0.6),
            pygame.Vector2(-0.9, 0.0),
            pygame.Vector2(-0.6, -0.5),
            pygame.Vector2(-0.2, -0.9),
            pygame.Vector2(0.4, -0.8),
            pygame.Vector2(0.9, -0.4),
        ],

        # Asteroid 20 – Compact irregular blob
        [
            pygame.Vector2(0.8, 0.0),
            pygame.Vector2(0.5, 0.7),
            pygame.Vector2(-0.1, 0.8),
            pygame.Vector2(-0.7, 0.5),
            pygame.Vector2(-0.9, 0.0),
            pygame.Vector2(-0.5, -0.7),
            pygame.Vector2(0.0, -0.9),
            pygame.Vector2(0.6, -0.6),
        ],
    ]

    shape_index = 0

    def __init__(self):
        super().__init__()
        self.shape_index = randint(0, len(self.asteroid_shapes) - 1)

    def calc(self, position, rotation, radius, dt):
        shape = self.asteroid_shapes[self.shape_index]
        self.points = [(point.rotate(rotation) * radius + position)
                       for point in shape]
        self.color = ASTEROID_COLOR
        self.thickness = ASTEROID_THICKNESS
