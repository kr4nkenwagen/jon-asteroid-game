from entity import entity
from player_thrust_polygon import player_thrust_polygon


class player_thrust_representation(entity):
    show = False

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.polygon = player_thrust_polygon()

    def update(self):
        self.polygon.enabled = self.show
