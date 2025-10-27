from random import randint
from asteroid_polygon import asteroid_polygon
from constants import ASTEROID_CHILD_DIVIDER, ASTEROID_CHILD_VELOCITY_MULTIPLIER, ASTEROID_LIFETIME, ASTEROID_MAX_ROTATION_SPEED, ASTEROID_MIN_RADIUS, ASTEROID_MIN_RADIUS_SPAN, SCORE_MULTIPLIER
from entity import entity


class asteroid(entity):
    player = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.collideable = True
        self.polygon = asteroid_polygon()
        self.angular_velocity = randint(-ASTEROID_MAX_ROTATION_SPEED, ASTEROID_MAX_ROTATION_SPEED)
        self.use_physics = True
        self.destroyed_by_player = True
        self.rotation_speed = 0
        self.life_timer = 0

    def update(self):
        if self.player == None:
            self.player = self.game.ent_manager.get_entity("player")
        if self.player:
            self.position += self.player.velocity * self.game.dt * -1
        self.life_timer += self.game.dt
        if self.life_timer > ASTEROID_LIFETIME:
            self.destroyed_by_player = False 
            self.game.ent_manager.remove_entity(self)

    def on_collision_enter(self, entity, collision_point):
        self.velocity = (self.position + self.velocity).reflect(entity.position).normalize() * self.velocity.length() 

    def on_destroy(self):
        if self.destroyed_by_player == False:
            return
        self.player.score += SCORE_MULTIPLIER / self.radius 
        if self.radius < ASTEROID_MIN_RADIUS + ASTEROID_MIN_RADIUS_SPAN:
            return
        child_count = self.radius // ASTEROID_CHILD_DIVIDER
        entities = []
        for x in range(child_count // 2):
            x_pos = self.position.x + (-(self.radius / 2) + (x * (self.radius / (child_count // 2))))
            for y in range(child_count // 2):
                y_pos = self.position.y + (-(self.radius / 2) + (y * (self.radius / (child_count // 2))))
                cur_ent = asteroid(x_pos, y_pos, self.radius // (ASTEROID_CHILD_DIVIDER * .5))
                cur_ent.velocity = self.velocity + ((cur_ent.position - self.position) * ASTEROID_CHILD_VELOCITY_MULTIPLIER)
                entities.append(cur_ent)
        self.game.ent_manager.add_entities(entities)
