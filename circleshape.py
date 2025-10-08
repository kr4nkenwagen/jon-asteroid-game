import pygame

class CircleShape(pygame.sprite.Sprite):
    rotation = 0
    position = pygame.Vector2(0, 0)
    velocity = pygame.Vector2(0, 0)
    radius = 0
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.radius = radius
    
    def update(self, dt):

        pass

    def draw(self, screen):
        pass


