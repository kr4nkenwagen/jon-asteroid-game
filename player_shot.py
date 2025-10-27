from constants import LASER_LIFETIME, LASTER_MAX_LENGTH
from entity import entity
from player_shot_polygon import player_shot_polygon
import pygame

class player_shot(entity):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, 1)
        self.rotation = rotation
        self.first_frame = True
        self.polygon = player_shot_polygon()
        self.lifetime = 0

    def update(self):
        if self.first_frame:
            distance = LASTER_MAX_LENGTH
            target, distance = self.game.coll_manager.polygon_raycast(self.position, self.rotation, distance, 5, 1)
            self.position = self.position + (pygame.Vector2(0,1).rotate(self.rotation) * distance / 2)
            self.polygon.length = distance
            if target != None:
                if target.__class__.__name__ == "asteroid":
                    target.hit()
            self.first_frame = False
        self.lifetime += self.game.dt
        if self.lifetime > LASER_LIFETIME:
            self.game.ent_manager.remove_entity(self)
 
