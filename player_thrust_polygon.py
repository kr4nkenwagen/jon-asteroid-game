from constants import PLAYER_RADIUS, PLAYER_REAR_THRUST_COLOR, PLAYER_REAR_THRUST_FLAME_PADDING, PLAYER_REAR_THRUST_FLAME_UPDATE_RATE, PLAYER_REAR_THRUST_THICKNESS
import polygon
import pygame
import random
from polygon import polygon

class player_thrust_polygon(polygon):
    def __init__(self):
        super().__init__()
        self.timer = PLAYER_REAR_THRUST_FLAME_UPDATE_RATE
        self.flame = []

    def calc(self, position, rotation, radius, dt):
       self.color = PLAYER_REAR_THRUST_COLOR
       self.thickness = PLAYER_REAR_THRUST_THICKNESS
       self.timer += dt
       if self.timer > PLAYER_REAR_THRUST_FLAME_UPDATE_RATE:
           self.randomize_flame()
           self.timer = 0
       flame_offset = pygame.Vector2(0, -PLAYER_RADIUS  + 1)
       self.points = []
       self.points = [position + (flame_offset + p).rotate(rotation) for p in self.flame]


    def randomize_flame(self):
        num_points = random.randint(3, 7)
        flame_width = PLAYER_RADIUS - (PLAYER_REAR_THRUST_FLAME_PADDING * 2)
        flame_length = 15
        flame_unifier = -flame_width // 2
        self.flame = []
        self.flame.append(pygame.Vector2(-flame_width, 0))
        for i in range(num_points):
            spread = random.randint(0, flame_width // num_points)
            depth = random.randint(5, flame_length)
            self.flame.append(pygame.Vector2(flame_unifier + spread, -depth))
            flame_unifier += flame_width // num_points
        self.flame.append(pygame.Vector2(flame_width, 0))

