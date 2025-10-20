from asteroid_polygon import asteroid_polygon
from constants import ASTEROID_LIFETIME
from entity import entity


class asteroid(entity):
    life_timer = 0
    player = None
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.collideable = True
        self.polygon = asteroid_polygon()

    def update(self):
        if self.player == None:
            self.player = self.game.ent_manager.get_entity("player")
        self.position += self.velocity * self.game.dt
        if self.player:
            self.position += self.player.velocity * self.game.dt * -1
        self.life_timer += self.game.dt
        if self.life_timer > ASTEROID_LIFETIME:
            print("asteroid exceeded its lifetime")
            self.game.ent_manager.remove_entity(self)

    def on_collision(self, entity):
        self.velocity = (self.position + self.velocity).reflect(entity.position).normalize() * self.velocity.length() 
