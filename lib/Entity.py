import pygame
from lib.constants import ENTITY_SIZE
from lib.Rectangle import AccelRectangle
from lib.Vector import Vector

class Entity(AccelRectangle):
    def __init__(self, pos):
        super().__init__(pos, Vector(ENTITY_SIZE))

    def render(self, screen, color):
        params = [self.pos.x, self.pos.y, ENTITY_SIZE, ENTITY_SIZE]
        pygame.draw.ellipse(screen, color, params)
