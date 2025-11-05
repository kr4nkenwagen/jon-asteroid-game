from random import randint
from constants import ASTEROID_COLOR, ASTEROID_THICKNESS
from polygon import polygon
from pygame import Vector2


class asteroid_polygon(polygon):
    asteroid_shapes = [
        # Asteroid 1 – Irregular pentagon
        [
            Vector2(0.8, 0),
            Vector2(0.4, 0.6),
            Vector2(-0.2, 0.8),
            Vector2(-0.9, 0.3),
            Vector2(-0.6, -0.7),
            Vector2(0.1, -0.9),
        ],

        # Asteroid 2 – More compact with bulges
        [
            Vector2(0.9, -0.1),
            Vector2(0.5, 0.5),
            Vector2(0.2, 0.9),
            Vector2(-0.4, 0.6),
            Vector2(-0.7, 0.2),
            Vector2(-0.6, -0.4),
            Vector2(-0.1, -0.8),
            Vector2(0.4, -0.6),
        ],

        # Asteroid 3 – Elongated, pointy
        [
            Vector2(1.0, 0.0),
            Vector2(0.6, 0.7),
            Vector2(0.0, 1.0),
            Vector2(-0.5, 0.8),
            Vector2(-1.0, 0.1),
            Vector2(-0.6, -0.6),
            Vector2(0.0, -1.0),
            Vector2(0.7, -0.5),
        ],

        # Asteroid 4 – Symmetrical but lumpy
        [
            Vector2(0.7, -0.2),
            Vector2(1.0, 0.2),
            Vector2(0.6, 0.7),
            Vector2(0.0, 1.0),
            Vector2(-0.6, 0.7),
            Vector2(-1.0, 0.0),
            Vector2(-0.5, -0.7),
            Vector2(0.0, -1.0),
        ],

        # Asteroid 5 – Chaotic and jagged
        [
            Vector2(0.8, 0.1),
            Vector2(0.5, 0.9),
            Vector2(-0.2, 0.7),
            Vector2(-0.9, 0.2),
            Vector2(-0.5, -0.3),
            Vector2(-0.7, -0.8),
            Vector2(0.1, -0.6),
            Vector2(0.6, -0.4),
        ],

        # Asteroid 6 – Smooth hexagon
        [
            Vector2(0.9, 0.0),
            Vector2(0.45, 0.8),
            Vector2(-0.45, 0.8),
            Vector2(-0.9, 0.0),
            Vector2(-0.45, -0.8),
            Vector2(0.45, -0.8),
        ],

        # Asteroid 7 – Squashed oval
        [
            Vector2(1.0, 0.0),
            Vector2(0.7, 0.6),
            Vector2(0.0, 0.8),
            Vector2(-0.7, 0.6),
            Vector2(-1.0, 0.0),
            Vector2(-0.8, -0.5),
            Vector2(0.0, -0.7),
            Vector2(0.8, -0.5),
        ],

        # Asteroid 8 – Cratered look
        [
            Vector2(0.9, 0.0),
            Vector2(0.6, 0.4),
            Vector2(0.2, 0.8),
            Vector2(-0.4, 0.9),
            Vector2(-0.8, 0.2),
            Vector2(-0.6, -0.6),
            Vector2(0.0, -1.0),
            Vector2(0.7, -0.4),
        ],

        # Asteroid 9 – Shattered rock
        [
            Vector2(1.0, 0.1),
            Vector2(0.6, 0.8),
            Vector2(0.1, 1.0),
            Vector2(-0.5, 0.7),
            Vector2(-0.9, 0.0),
            Vector2(-0.7, -0.6),
            Vector2(-0.2, -1.0),
            Vector2(0.4, -0.8),
            Vector2(0.8, -0.3),
        ],

        # Asteroid 10 – Chunky and asymmetrical
        [
            Vector2(0.9, -0.3),
            Vector2(0.7, 0.6),
            Vector2(0.0, 1.0),
            Vector2(-0.6, 0.7),
            Vector2(-0.9, -0.1),
            Vector2(-0.5, -0.8),
            Vector2(0.3, -0.9),
            Vector2(0.9, -0.5),
        ],

        # Asteroid 11 – Compact and rocky
        [
            Vector2(0.8, 0.2),
            Vector2(0.5, 0.7),
            Vector2(-0.2, 0.8),
            Vector2(-0.8, 0.4),
            Vector2(-0.7, -0.3),
            Vector2(-0.2, -0.9),
            Vector2(0.4, -0.7),
            Vector2(0.9, -0.2),
        ],

        # Asteroid 12 – Tri-lobed
        [
            Vector2(1.0, 0.0),
            Vector2(0.0, 1.0),
            Vector2(-1.0, 0.0),
            Vector2(0.0, -0.8),
        ],

        # Asteroid 13 – Fragmented ring
        [
            Vector2(0.9, 0.1),
            Vector2(0.6, 0.7),
            Vector2(-0.2, 0.9),
            Vector2(-0.9, 0.3),
            Vector2(-0.8, -0.4),
            Vector2(-0.3, -0.9),
            Vector2(0.5, -0.8),
            Vector2(0.9, -0.3),
        ],

        # Asteroid 14 – Very elongated
        [
            Vector2(1.0, 0.0),
            Vector2(0.8, 0.3),
            Vector2(0.3, 0.6),
            Vector2(-0.3, 0.5),
            Vector2(-1.0, 0.0),
            Vector2(-0.5, -0.4),
            Vector2(0.4, -0.5),
            Vector2(0.9, -0.2),
        ],

        # Asteroid 15 – Chunky triangle
        [
            Vector2(0.9, -0.2),
            Vector2(0.2, 0.9),
            Vector2(-0.8, 0.5),
            Vector2(-0.9, -0.3),
            Vector2(-0.1, -0.9),
            Vector2(0.7, -0.7),
        ],

        # Asteroid 16 – Compact lump
        [
            Vector2(0.7, 0.0),
            Vector2(0.5, 0.5),
            Vector2(-0.2, 0.8),
            Vector2(-0.7, 0.3),
            Vector2(-0.8, -0.3),
            Vector2(-0.2, -0.7),
            Vector2(0.3, -0.8),
            Vector2(0.8, -0.3),
        ],

        # Asteroid 17 – Jagged crystal
        [
            Vector2(1.0, 0.0),
            Vector2(0.7, 0.6),
            Vector2(0.0, 0.9),
            Vector2(-0.6, 0.5),
            Vector2(-0.9, -0.1),
            Vector2(-0.6, -0.7),
            Vector2(0.0, -1.0),
            Vector2(0.6, -0.8),
        ],

        # Asteroid 18 – Flattened slab
        [
            Vector2(1.0, 0.0),
            Vector2(0.8, 0.3),
            Vector2(0.2, 0.5),
            Vector2(-0.2, 0.5),
            Vector2(-0.8, 0.3),
            Vector2(-1.0, 0.0),
            Vector2(-0.8, -0.3),
            Vector2(-0.2, -0.5),
            Vector2(0.8, -0.3),
        ],

        # Asteroid 19 – Highly irregular
        [
            Vector2(0.9, 0.1),
            Vector2(0.6, 0.8),
            Vector2(0.0, 0.9),
            Vector2(-0.7, 0.6),
            Vector2(-0.9, 0.0),
            Vector2(-0.6, -0.5),
            Vector2(-0.2, -0.9),
            Vector2(0.4, -0.8),
            Vector2(0.9, -0.4),
        ],

        # Asteroid 20 – Compact irregular blob
        [
            Vector2(0.8, 0.0),
            Vector2(0.5, 0.7),
            Vector2(-0.1, 0.8),
            Vector2(-0.7, 0.5),
            Vector2(-0.9, 0.0),
            Vector2(-0.5, -0.7),
            Vector2(0.0, -0.9),
            Vector2(0.6, -0.6),
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
