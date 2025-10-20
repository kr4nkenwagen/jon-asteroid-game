from constants import PLAYER_RADIUS
import pygame
from polygon import polygon

class player_polygon(polygon):
    def calc(self, position, rotation, radius):
        right = pygame.Vector2(0, 1).rotate(rotation + 90) * PLAYER_RADIUS
        forward = pygame.Vector2(0, 1).rotate(rotation)
        a = position + forward * PLAYER_RADIUS 
        b = position - forward * PLAYER_RADIUS - right
        c = position - forward * PLAYER_RADIUS + right
        self.points = [a, b, c]

