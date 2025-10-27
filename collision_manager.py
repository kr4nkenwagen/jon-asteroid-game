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
                        radius = (cur_ent.radius + sec_ent.radius) / 2
                        if dist < radius:
                            if self.polygons_collide(cur_ent.polygon.points, sec_ent.polygon.points):
                                if sec_ent.id not in cur_ent.has_collided_with:
                                    collision_point = self.get_collision_point(cur_ent.polygon.points, sec_ent.polygon.points)
                                    cur_ent.on_collision_enter(sec_ent, collision_point)
                                    sec_ent.on_collision_enter(cur_ent, collision_point)
                                else:
                                    cur_ent.on_collision(sec_ent)
                                    sec_ent.on_collision(cur_ent)
                                cur_ent.has_collided_with.add(sec_ent.id)
                                sec_ent.has_collided_with.add(cur_ent.id)
                            else:
                                if sec_ent.id in cur_ent.has_collided_with:
                                    cur_ent.has_collided_with.discard(sec_ent.id)
                                    cur_ent.on_collision_exit(sec_ent)
                                if cur_ent.id in sec_ent.has_collided_with:
                                    sec_ent.has_collided_with.discard(cur_ent.id)
                                    sec_ent.on_collision_exit(cur_ent)
                    sec_ent = sec_ent.next
            cur_ent = cur_ent.next

    def polygons_collide(self, pol1, pol2):
        for polygon in [pol1, pol2]:
            for i1 in range(len(polygon)):
                i2 = (i1 + 1) % len(polygon)
                p1 = polygon[i1]
                p2 = polygon[i2]
                edge = p2 - p1
                axis = pygame.Vector2(0, 0)
                if edge.y != 0 and edge.x != 0:
                    axis = pygame.Vector2(-edge.y, edge.x).normalize()
                min_a, max_a = self.polygon_projection(pol1, axis)
                min_b, max_b = self.polygon_projection(pol2, axis)
                if max_a < min_b or max_b < min_a:
                    return False
        return True 

    def polygon_projection(self, pol, axis):
        dots = [point.dot(axis) for point in pol]
        return min(dots), max(dots)

    def get_collision_point(self, pol1, pol2):
        min_dist = float('inf')
        for p1 in pol1:
            for p2 in pol2:
                dist = p1.distance_to(p2)
                if dist < min_dist:
                    min_dist = dist
                    return pygame.Vector2(p1.x / p2.x, p1.y / p2.y)
        return pygame.Vector2(0, 0) 
    
    def shift_points(self, points, shift, rotation):
        return [p + shift.rotate(rotation) for p in points]

    def check_velocity_position(self, entity):
        if len(entity.polygon.points) == 0:
            return None 
        cur_ent = entity.next
        while cur_ent != None:
            if cur_ent != entity and cur_ent.use_physics and len(cur_ent.polygon.points) > 0:
                dist = (cur_ent.position + cur_ent.velocity).distance_to(entity.position + entity.velocity)
                radius = cur_ent.radius + entity.radius
                if dist < radius:
                    p1 = self.shift_points(cur_ent.polygon.points, cur_ent.velocity * self.game.dt, cur_ent.angular_velocity * self.game.dt)
                    p2 = self.shift_points(entity.polygon.points, entity.velocity * self.game.dt, entity.angular_velocity * self.game.dt)
                    if self.polygons_collide(p1, p2):
                        return cur_ent
            cur_ent = cur_ent.next
        return None 

    def polygon_line(self, position, rotation, length, thickness):
        half_length = length / 2 
        half_thickness = thickness / 2
        points = [
           pygame.Vector2(-half_length, -half_thickness),
           pygame.Vector2(half_length, -half_thickness),
           pygame.Vector2(half_length, half_thickness),
           pygame.Vector2(-half_length, half_thickness)
        ]
        points = [position + p.rotate(rotation) for p in points]
        pygame.draw.polygon(self.game.screen, "red", points, 20)
        return points

    def polygon_raycast(self, origin, direction, max_distance, step, width):
        distance = 0
        while distance < max_distance:
            ray_center = origin + (pygame.Vector2(0, 1).rotate(direction) * distance)
            ray = self.polygon_line(ray_center, direction, step, width)
            cur_ent = self.game.ent_manager.first_entity
            while cur_ent != None:
                if cur_ent.collideable and len(cur_ent.polygon.points) > 0:
                    if self.polygons_collide(ray, cur_ent.polygon.points):
                        return cur_ent, distance
                cur_ent = cur_ent.next
            distance += step
        return None, distance
