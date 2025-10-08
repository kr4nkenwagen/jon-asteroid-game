import pygame

class entity(pygame.sprite.Sprite):
    next = None
    game = None
    id = 0
    rotation = 0
    position = pygame.Vector2(0, 0)
    velocity = pygame.Vector2(0, 0)
    radius = 0
    polygon = None
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.radius = radius
    
    def update(self):

        pass

    def draw(self):
        pass


