from constants import PLAYER_RADIUS
import polygon
import pygame
import random

class player_thrust_polygon:
    def calc(self, position, rotation, radius):
        self.color = "yellow"
        self.thickness = 1
        offset = pygame.Vector2(PLAYER_RADIUS // 3, PLAYER_RADIUS + 10)
        a = (pygame.Vector2(random.randint(-2, 2), 10) - offset).rotate(rotation) + position
        b = (pygame.Vector2(PLAYER_RADIUS + random.randint(-2, 2), 10) - offset).rotate(rotation) + position
        top_c = (pygame.Vector2(PLAYER_RADIUS - 5 + random.randint(-2, 2), random.randint(-2, 2)) - offset).rotate(rotation) + position
        d = (pygame.Vector2(PLAYER_RADIUS - 10, random.randint(3, 7)) - offset).rotate(rotation) + position
        top_e = (pygame.Vector2(PLAYER_RADIUS // 2 + random.randint(-2, 2), random.randint(-2, 2)) - offset).rotate(rotation) + position
        self.points = [ a,  b, top_c, d, top_e  ]

