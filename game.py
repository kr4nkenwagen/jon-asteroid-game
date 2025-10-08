from asteroid_spawner import asteroid_spawner
from constants import * 
from entity_manager import entity_manager
from player import player
import pygame

from typing import dataclass_transform
import pygame

class game():
    screen = None
    clock = None
    dt = 0
    ent_manager = None
    game_running = False
    def init(self):
        print("Starting Asteroids!")
        print("Screen width: " + str(SCREEN_WIDTH))
        print("Screen height: " + str(SCREEN_HEIGHT))
        pygame.init()
        self.ent_manager = entity_manager(self)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.ent_manager.add_entity(player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.ent_manager.add_entity(asteroid_spawner())
        self.game_running = True
     
    def update(self):
        self.ent_manager.update()
        self.dt = self.clock.tick() / 1000
    
    def draw(self):
        self.ent_manager.draw()

    def end(self):
        print("game closing")
