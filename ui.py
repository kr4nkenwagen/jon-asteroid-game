from entity import entity
from ui_score import ui_score

class ui(entity):
    def __init__(self):
        super().__init__(0, 0, 0)
        self. initialized = False

    def update(self):
        if self.initialized == False:
            self.game.ent_manager.add_entity(ui_score())
            self.initialized = True
