import time
from lib.constants import COLOR_BLACK, ENTITY_SIZE, FONT_NORMAL
from lib.Entity import Entity
from lib.Vector import Vector

class Enemy(Entity):
    def __init__(self, pos):
        super().__init__(pos)
        self.is_target = False

    def render(self, game, color=None):
        super().render(game.screen, self.get_color())
        text = str(time.time() - self.creation_time)[0:4]
        pos = Vector(self.pos.x + (ENTITY_SIZE / 4), self.pos.y + (ENTITY_SIZE / 2) - 5)
        game.draw_text(FONT_NORMAL, text, pos, COLOR_BLACK)

    def get_color(self):
        blue = 0xFF * (time.time() - self.creation_time) / 20
        if self.is_target:
            return (0xFF, 0x00, blue)
        else:
            return (0x00, 0xFF, blue)
