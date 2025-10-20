import pygame
from entity import entity

class collision_manager():
    game = None
    def __init__(self, game):
        self.game = game

    def update(self):
        cur_ent = self.game.ent_manager.first_entity
        while cur_ent != None:
            if cur_ent.collideable:
                sec_ent = cur_ent.next
                while sec_ent != None:
                    if sec_ent.collideable:
                        if cur_ent.position.distance_to(sec_ent.position) < cur_ent.radius + sec_ent.radius:
                            if cur_ent.has_collided_with.count(sec_ent.id) == 0:
                                cur_ent.on_collision(sec_ent)
                                sec_ent.on_collision(cur_ent)
                                cur_ent.has_collided_with.append(sec_ent.id)
                        else:
                            while cur_ent.has_collided_with.count(sec_ent.id) > 0:
                                cur_ent.has_collided_with.remove(sec_ent.id)
                    sec_ent = sec_ent.next
            cur_ent = cur_ent.next
