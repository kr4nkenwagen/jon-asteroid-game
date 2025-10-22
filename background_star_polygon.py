from constants import BACKGROUND_SPEED_MULTIPLIER, BACKGROUND_STAR_COLOR, BACKGROUND_STAR_DISTORTION_LIMIT, BACKGROUND_STAR_DISTORTION_MAX_LENGTH
from polygon import polygon
import pygame

class background_star_polygon(polygon):
    def __init__(self, layer):
        super().__init__()
        self.layer = layer
        self.velocity = pygame.Vector2(0, 0)

    def calc(self, position, rotation, radius):
        self.thickness = 1
        self.color = BACKGROUND_STAR_COLOR
        length = 0
        rotation = self.velocity.as_polar()[1] + 90
        if self.velocity.length() >= BACKGROUND_STAR_DISTORTION_LIMIT:
            length = (self.velocity.length() - BACKGROUND_STAR_DISTORTION_LIMIT) * (self.layer * BACKGROUND_SPEED_MULTIPLIER) * BACKGROUND_STAR_DISTORTION_MAX_LENGTH
        self.points = [ pygame.Vector2(0, 0), pygame.Vector2(1, 0), pygame.Vector2(1, 1 + length), pygame.Vector2(0, 1 + length) ]
        self.points  = [position + p.rotate(rotation) for p in self.points]
