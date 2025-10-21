from random import randint
from asteroid_polygon import asteroid_polygon
from constants import ASTEROID_LIFETIME, ASTEROID_MAX_ROTATION_SPEED
from entity import entity


class asteroid(entity):
    life_timer = 0
    player = None
    rotation_speed = 0
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.collideable = True
        self.polygon = asteroid_polygon()
        self.rotation_speed = randint(-ASTEROID_MAX_ROTATION_SPEED, ASTEROID_MAX_ROTATION_SPEED)

    def update(self):
        if self.player == None:
            self.player = self.game.ent_manager.get_entity("player")
        self.position += self.velocity * self.game.dt
        self.rotation += self.rotation_speed * self.game.dt
        if self.player:
            self.position += self.player.velocity * self.game.dt * -1
        self.life_timer += self.game.dt
        if self.life_timer > ASTEROID_LIFETIME:
            print("asteroid exceeded its lifetime")
            self.game.ent_manager.remove_entity(self)

    def on_collision_enter(self, entity, collision_point):
        self.velocity = (self.position + self.velocity).reflect(entity.position).normalize() * self.velocity.length() 
