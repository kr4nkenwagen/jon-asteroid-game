import pygame

class entity(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        self.position = pygame.Vector2(x, y)
        self.next = None
        self.game = None
        self.parent = None
        self.collideable = False
        self.has_collided_with = set()
        self.id = 0
        self.rotation = 0
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = 0
        self.radius = radius
        self.polygon = None
    
    def update(self):

        pass

    def draw(self):
        pass


    def on_collision(self, entity):
        pass
