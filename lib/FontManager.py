import pygame

class FontManager(object):
    def __init__(self):
        self.fonts = {}

    def get(self, size):
        if size not in self.fonts:
            self.fonts[size] = pygame.font.Font(None, size)
        return self.fonts[size]
