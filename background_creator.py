from random import randint
from background_star import background_star
from constants import BACKGROUND_MAX_STARS, BACKGROUND_MIN_STARS
import pygame
from entity import entity

class background_creator(entity):
    def __init__(self):
        super().__init__(0, 0, 0)

    def update(self):
        amount = randint(BACKGROUND_MIN_STARS, BACKGROUND_MAX_STARS)
        while amount > 0:
            self.game.ent_manager.add_entity(background_star())
            amount -= 1
        self.game.ent_manager.remove_entity(self)
