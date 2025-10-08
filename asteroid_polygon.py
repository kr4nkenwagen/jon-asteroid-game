from polygon import polygon
import pygame

class asteroid_polygon(polygon):

    def calc(self, position, rotation, radius):
        half_rad = radius // 2
        a = position + pygame.Vector2(-half_rad, -half_rad) 
        b = position + pygame.Vector2(-half_rad, half_rad)
        c = position + pygame.Vector2(half_rad, half_rad) 
        d = position + pygame.Vector2(half_rad, -half_rad)
        self.points = [a, b, c, d]
