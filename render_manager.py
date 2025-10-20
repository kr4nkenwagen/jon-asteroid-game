import pygame

class render_manager():
    game = None
    render_queue = []
    def __init__(self, game):
        self.game = game

    def add_queue(self, polygon):
        self.render_queue.append(polygon)

    def draw(self):
        self.game.screen.fill("black")
        self.game.ent_manager.draw()
        for pol in self.render_queue:
            pygame.draw.polygon(self.game.screen, pol.color, pol.points, pol.thickness)
        pygame.display.flip()
        self.render_queue.clear()
