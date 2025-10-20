from polygon import polygon
import pygame

class background_star_polygon(polygon):
    def calc(self, position, rotation, radius):
        self.points = [ position + pygame.Vector2(0, 0), position + pygame.Vector2(1, 0), position + pygame.Vector2(1, 1), position + pygame.Vector2(0, 1) ]
        self.color = "white"
        self.thickness = 2
