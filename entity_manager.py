import pygame

class entity_manager:
    first_entity = None
    id_count = 0
    def __init__(self, game):
        self.game = game
        pass

    def update(self):
        curr_ent = self.first_entity
        while curr_ent != None:
            if curr_ent.parent != None:
                curr_ent.position = curr_ent.parent.position.copy()
                curr_ent.rotation = curr_ent.parent.rotation
                curr_ent.radius = curr_ent.parent.radius
            curr_ent.update()
            curr_ent = curr_ent.next
    
    def draw(self):
        curr_ent = self.first_entity
        while curr_ent != None:
            if curr_ent.polygon != None and curr_ent.polygon.enabled:
                curr_ent.polygon.calc(curr_ent.position, curr_ent.rotation, curr_ent.radius, self.game.dt)
                self.game.rendr_manager.add_queue(curr_ent.polygon)
            curr_ent.draw()
            curr_ent = curr_ent.next

    def update_physics(self):
        curr_ent = self.first_entity
        while curr_ent != None:
            if curr_ent.use_physics:
                op = self.game.coll_manager.check_velocity_position(curr_ent)
                if op == None:
                    curr_ent.position += curr_ent.velocity * self.game.dt
                else:
                    self.physics_bounce(curr_ent, op)
            curr_ent = curr_ent.next

    def add_entity(self, entity):
        entity.game = self.game
        entity.id = self.id_count
        self.id_count += 1
        if self.first_entity == None:
            self.first_entity = entity
            return entity
        curr_ent = self.first_entity
        while curr_ent.next != None:
            curr_ent = curr_ent.next
        curr_ent.next = entity
        return entity

    def remove_entity(self, entity):
        if entity == None:
            return
        if self.first_entity.id == entity.id:
            entity.next = self.first_entity.next
            self.first_entity = entity
            return
        curr_ent = self.first_entity
        while curr_ent != None:
            if curr_ent.next.id == entity.id:
                curr_ent.next = curr_ent.next.next
                return
            curr_ent = curr_ent.next

    def get_entity(self, name):
        curr_ent = self.first_entity
        while type(curr_ent).__name__ != name:
            curr_ent = curr_ent.next
        return curr_ent

    def physics_bounce(self, e1, e2):
        rel_vel = e1.velocity - e2.velocity
        normal = (e1.position - e2.position).normalize()
        vel_along = rel_vel.dot(normal)
        if vel_along > 0:
            return
        impulse = ((2 * vel_along) / (e1.radius + e2.radius)) * normal
        e1.velocity -= impulse * e2.radius
        e2.velocity += impulse * e1.radius
