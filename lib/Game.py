import time
import pygame
import pygame.locals as Pygame
# pylint: disable=I0011,W0614,W0401
from lib.constants import *
# pylint: disable=I0011,I0012; enable=W0614,W0401
from lib.Enemy import Enemy
from lib.FontManager import FontManager
from lib.Player import Player
from lib.Vector import Vector

class Game(object):
    def __init__(self):
        self.coords = []
        self.player = None
        self.enemies = []
        self.last_spawn_time = 0
        self.start_time = 0
        self.score = 0
        self.screen = None
        self.display_info = None
        self.clock = None
        self.font_mgr = None
        self.is_ended = False
        self.should_stop = False
        self.size = None
        self.background = None

    def start(self):
        self.start_time = time.time()
        pygame.init()
        pygame.mouse.set_visible(False)
        pygame.key.set_repeat(True)
        self.display_info = pygame.display.Info()
        self.screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        # pylint: disable=I0011,E1121
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill(BACKGROUND_COLOR)
        # pylint: disable=I0011,I0012; enable=E1121
        self.font_mgr = FontManager()
        self.size = Vector(self.screen.get_size()[0], self.screen.get_size()[1])
        self.clock = pygame.time.Clock()
        self.player = Player(self.size.div(2))
        self.spawn_enemy()
        self.loop()
        pygame.quit()

    def loop(self):
        while not self.should_stop:
            self.clock.tick(60)
            self.render()
            pygame.display.flip()
            self.update()
            for event in pygame.event.get():
                if event.type == Pygame.QUIT:
                    self.should_stop = True

    def render(self):
        self.screen.blit(self.background, (0, 0))
        if self.is_ended:
            self.draw_text(FONT_END, "You have lost!", Vector(0, 256), COLOR_BLUE)
            return
        now = time.time()
        for enemy in self.enemies:
            enemy.render(self)
        self.player.render(self.screen)
        acceleration_text = "Acceleration: {}".format(self.player.velocity)
        position_text = "Position: {}".format(self.player.pos)
        score_text = "Score: {}".format(self.score)
        hps_text = "Hits / Second: {}".format(str(self.score / (now - self.start_time))[0:6])
        end_text = "Press X to end the game."
        self.draw_text(FONT_NORMAL, acceleration_text, Vector(0, 0), COLOR_WHITE)
        self.draw_text(FONT_NORMAL, position_text, Vector(0, 16), COLOR_WHITE)
        self.draw_text(FONT_NORMAL, score_text, Vector(0, 32), COLOR_WHITE)
        self.draw_text(FONT_NORMAL, hps_text, Vector(0, 48), COLOR_WHITE)
        self.draw_text(FONT_NORMAL, end_text, Vector(0, 64), COLOR_WHITE)

    def update(self):
        now = time.time()
        if now - self.last_spawn_time > 0.5 and len(self.enemies) < MAX_ENEMY_COUNT:
            self.spawn_enemy()
        keys = pygame.key.get_pressed()
        if keys[Pygame.K_ESCAPE]:
            self.end()
            return
        if keys[Pygame.K_r] or keys[Pygame.K_z] or keys[Pygame.K_b]:
            self.player.is_bot = True
        self.player.update(self)
        for index in range(0, len(self.enemies)):
            if self.player.collides(self.enemies[index]):
                if self.player.target is not None and index < self.player.target:
                    self.player.target -= 1
                if self.enemies[index].is_target:
                    self.player.is_target_destroyed = True
                self.enemies.pop(index)
                self.score += 1
                break
            time_since_creation = now - self.enemies[index].creation_time
            if time_since_creation > TIME_TO_LOSE:
                self.end()
                return

    def end(self):
        print("ended: {}".format(self.score))

    def draw_text(self, size, text, pos, color):
        rendered = self.font_mgr.get(size).render(text, True, color)
        self.screen.blit(rendered, (pos.x, pos.y))

    def spawn_enemy(self):
        size = Vector(ENTITY_SIZE)
        pos = Vector.rand(size, self.size.sub(ENTITY_SIZE))
        enemy = Enemy(pos)
        self.enemies.append(enemy)
        self.last_spawn_time = time.time()
