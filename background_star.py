from random import randint
from background_star_polygon import background_star_polygon
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from entity import entity

class background_star(entity):
    def __init__(self, ):
        self.polygon = background_star_polygon()
        self.position.x = randint(0, SCREEN_WIDTH)
        self.position.y = randint(0, SCREEN_HEIGHT)
        super().__init__(self.position.x, self.position.y, 1)
