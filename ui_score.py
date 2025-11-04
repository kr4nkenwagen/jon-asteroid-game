from constants import LEVEL_LIMIT, SCREEN_HEIGHT, SCREEN_WIDTH, UI_OFFSET, UI_SCORE_HEIGHT, UI_SCORE_WIDTH
from entity import entity
import pygame


class ui_score(entity):
    def __init__(self):
        super().__init__(0, 0, 0)
        self.frame = pygame.Rect((SCREEN_WIDTH // 2) - UI_SCORE_WIDTH // 2,
                                 SCREEN_HEIGHT - UI_OFFSET + UI_SCORE_HEIGHT,
                                 UI_SCORE_WIDTH, UI_SCORE_HEIGHT)
        self.value_rect = pygame.Rect(
            self.frame.x, self.frame.y, 0, self.frame.height)
        self.player = None
        self.value = 0
        self.update_value = 0
        self.player_level = 0

    def update(self):
        if self.player is None:
            self.player = self.game.ent_manager.get_entity("player")
        if self.player_level != self.player.level:
            self.player_level = self.player.level
            self.update_value = LEVEL_LIMIT - self.value
        if self.value >= LEVEL_LIMIT - .001:
            self.value = 0
            self.update_value = 0
        if self.update_value > 0:
            diff = pygame.math.lerp(
                0, self.update_value, min(max(self.game.dt, 0), 1))
            self.update_value -= diff
            self.value += diff
            if diff < .001:
                diff = 0
        if self.value + self.update_value < self.player.score:
            self.update_value = self.player.score - self.value
        self.value_rect.width = (self.value / LEVEL_LIMIT) * UI_SCORE_WIDTH

    def draw(self):
        pygame.draw.rect(self.game.screen, "white", self.frame)
        pygame.draw.rect(self.game.screen, "green", self.value_rect)
        pygame.draw.rect(self.game.screen,
                         "blue",
                         pygame.Rect(self.value_rect.x + self.value_rect.width,
                                     self.value_rect.y,
                                     (self.update_value / LEVEL_LIMIT) *
                                     UI_SCORE_WIDTH,
                                     self.value_rect.height))
