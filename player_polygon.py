from constants import PLAYER_COLOR, PLAYER_RADIUS, PLAYER_THICKNESS
import pygame
from polygon import polygon


class player_polygon(polygon):
    def calc(self, position, rotation, radius, dt):
        right = pygame.Vector2(0, 1).rotate(rotation + 90)
        forward = pygame.Vector2(0, 1).rotate(rotation)
        r = PLAYER_RADIUS

        # Define detailed 7-point ship shape
        a = position + forward * r * 1.3
        b = position - forward * r * 0.3 + right * r * 0.4
        c = position - forward * r * 0.5 + right * r * 1.0
        d = position - forward * r * 0.9 + right * r * 0.3
        e = position - forward * r * 0.9 - right * r * 0.3
        f = position - forward * r * 0.5 - right * r * 1.0
        g = position - forward * r * 0.3 - right * r * 0.4

        self.points = [a, b, c, d, e, f, g]
        self.color = PLAYER_COLOR
        self.thickness = PLAYER_THICKNESS
