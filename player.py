from constants import LEVEL_LIMIT, PLAYER_ACCELERATION, PLAYER_DEACCELERATION, PLAYER_FIRE_RATE, PLAYER_MAX_SPEED, PLAYER_RADIUS,PLAYER_TURN_SPEED, SCREEN_ACCELERATION, SCREEN_DEACCELERATION, SCREEN_HEIGHT, SCREEN_OFFSET_LIMIT, SCREEN_WIDTH
from entity import entity
from player_polygon import player_polygon
from player_shot import player_shot
from player_thrust_polygon import player_thrust_polygon
from player_thurst_representation import player_thrust_representation
import pygame

class player(entity):
    thrust_representation = None
    camera_offset = pygame.Vector2(0, 0)
    player_fire_rate_counter = 0

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.polygon = player_polygon()
        self.collideable = True
        self.rotation = 180
        self.score = 0
        self.level = 0

    def forward(self):
        return pygame.Vector2(0, 1).rotate(self.rotation)
    
    def rotate(self, dt, keys):
        direction = 0;
        if keys[pygame.K_a]:
            direction += 1
        if keys[pygame.K_d]:
            direction -= 1
        self.rotation += direction * PLAYER_TURN_SPEED * dt

    def accelerate(self, dt):
        self.thrust_representation.show = True
        self.velocity = self.velocity.lerp(self.forward() * PLAYER_MAX_SPEED, PLAYER_ACCELERATION / PLAYER_MAX_SPEED * dt)
        if self.camera_offset.length() < SCREEN_OFFSET_LIMIT:
            self.camera_offset = self.camera_offset.lerp(self.forward() * SCREEN_OFFSET_LIMIT,  (SCREEN_ACCELERATION * dt) / SCREEN_OFFSET_LIMIT)

    def deaccelerate(self, dt):
        self.thrust_representation.show = False
        self.velocity = self.velocity.lerp(pygame.Vector2(0, 0), PLAYER_DEACCELERATION / PLAYER_MAX_SPEED * dt)
        if self.camera_offset.length() != 0:
            self.camera_offset = self.camera_offset.lerp(pygame.Vector2(0, 0), min((SCREEN_DEACCELERATION * dt) / self.camera_offset.length(), 1))

    def move(self, dt, keys):
        if keys[pygame.K_w]:
            self.accelerate(dt)
        else:
            self.deaccelerate(dt)
        self.position = self.camera_offset + pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def update(self):
        if self.thrust_representation == None:
            self.thrust_representation = self.game.ent_manager.add_entity(player_thrust_representation(self.position.x, self.position.y, 10))
            self.thrust_representation.parent = self
        keys = pygame.key.get_pressed()
        self.rotate(self.game.dt, keys)
        self.move(self.game.dt, keys)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.reload()
        if self.score > LEVEL_LIMIT:
            self.score = 0
            self.level += 1

    def shoot(self):
        if self.player_fire_rate_counter > 0:
            return
        origin = self.position + self.forward() * (self.radius + 10)
        self.game.ent_manager.add_entity(player_shot(origin.x, origin.y, self.rotation))
        self.player_fire_rate_counter += self.game.dt

    def reload(self):
        if self.player_fire_rate_counter > 0:
            self.player_fire_rate_counter += self.game.dt
            if self.player_fire_rate_counter > PLAYER_FIRE_RATE:
                self.player_fire_rate_counter = 0


    def on_collision_enter(self, entity, collision_point):
        print("Player collided with " + str(entity.id))
        #self.velocity = entity.velocity * -1 * 10

    def on_collision(self, entity):
        pass

    def on_collision_exit(self, entity):
        print("Player collision with " + str(entity.id) + " ended")
