import pygame
from entity import entity

class collision_manager():
    game = None
    def __init__(self, game):
        self.game = game

    def update(self):
        cur_ent = self.game.ent_manager.first_entity
        while cur_ent != None:
            if cur_ent.collideable and len(cur_ent.polygon.points) > 0:
                sec_ent = cur_ent.next
                while sec_ent != None:
                    if sec_ent.collideable and len(sec_ent.polygon.points) > 0:
                        dist = cur_ent.position.distance_to(sec_ent.position)
                        radius = cur_ent.radius + sec_ent.radius
                        if dist < radius:
                            if self.polygons_collide(cur_ent.polygon.points, sec_ent.polygon.points):
                                if sec_ent.id not in cur_ent.has_collided_with:
                                    cur_ent.on_collision(sec_ent)
                                    sec_ent.on_collision(cur_ent)
                                cur_ent.has_collided_with.add(sec_ent.id)
                                sec_ent.has_collided_with.add(cur_ent.id)
                            else:
                                if sec_ent.id in cur_ent.has_collided_with:
                                    cur_ent.has_collided_with.discard(sec_ent.id)
                                if cur_ent.id in sec_ent.has_collided_with:
                                    sec_ent.has_collided_with.discard(cur_ent.id)
                    sec_ent = sec_ent.next
            cur_ent = cur_ent.next

    def polygons_collide(self, pol1, pol2):
        for polygon in [pol1, pol2]:
            for i1 in range(len(polygon)):
                i2 = (i1 + 1) % len(polygon)
                p1 = polygon[i1]
                p2 = polygon[i2]
                edge = p2 - p1
                axis = pygame.Vector2(-edge.y, edge.x).normalize()
                min_a, max_a = self.polygon_projection(pol1, axis)
                min_b, max_b = self.polygon_projection(pol2, axis)
                if max_a < min_b or max_b < min_a:
                    return False
        return True 

    def polygon_projection(self, pol, axis):
        dots = [point.dot(axis) for point in pol]
        return min(dots), max(dots)

