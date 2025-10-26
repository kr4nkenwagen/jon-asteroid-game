from constants import BACKGROUND_COLOR, DEBUG_ENABLED
import pygame

class render_manager():
    game = None
    render_queue = []
    def __init__(self, game):
        self.game = game

    def add_queue(self, polygon):
        self.render_queue.append(polygon)

    def draw(self):
        if DEBUG_ENABLED == False:
            self.game.screen.fill(BACKGROUND_COLOR)
        self.game.ent_manager.draw()
        for pol in self.render_queue:
            if pol.show:
                pygame.draw.polygon(self.game.screen, pol.color, pol.points, pol.thickness)
        pygame.display.flip()
        self.render_queue.clear()
