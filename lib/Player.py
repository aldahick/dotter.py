import time
import pygame
import pygame.locals as Pygame
# pylint: disable=I0011,W0614,W0401
from lib.constants import *
# pylint: disable=I0011,I0012; enable=W0614,W0401
from lib.Entity import Entity
from lib.Vector import Vector

class Player(Entity):
    def __init__(self, pos):
        super().__init__(pos)
        self.target = None
        self.is_target_destroyed = False
        self.is_bot = False
        self.trail = []

    def render(self, screen, color=None):
        super().render(screen, PLAYER_COLOR)
        for coord in self.trail:
            params = [coord.x, coord.y, ENTITY_SIZE / 4, ENTITY_SIZE / 4]
            pygame.draw.ellipse(screen, TRAIL_COLOR, params)

    def find_target(self, enemies):
        if not self.is_bot:
            return
        if self.target is not None and self.is_target_destroyed is False:
            return
        if len(enemies) == 0:
            return
        targets = []
        now = time.time()
        has_priority = False
        for index in range(0, len(enemies)):
            distance = self.get_distance(enemies[index])
            time_left = now - enemies[index].creation_time
            is_priority = TIME_TO_LOSE / 2 <= time_left
            targets.append({
                "index": index,
                "distance": distance,
                "is_priority": is_priority
            })
            if is_priority:
                has_priority = True
        closest = targets[0]
        for target in targets:
            if has_priority and not target["is_priority"]:
                continue
            if target["distance"] < closest["distance"]:
                closest = target
        self.target = closest["index"]
        self.is_target_destroyed = False
        enemies[self.target].is_target = True

    def move_bot(self, game):
        self.find_target(game.enemies)
        distance = self.get_distance_components(game.enemies[self.target])
        target_pos = game.enemies[self.target].pos
        if target_pos.x is not self.pos.x:
            target_greater = target_pos.x > self.pos.x
            if distance.x > 4 or self.velocity.x < 0:
                self.accelerate(Direction.RIGHT if target_greater else Direction.LEFT)
            else:
                self.accelerate(Direction.LEFT if target_greater else Direction.RIGHT)
        if target_pos.y is not self.pos.y:
            target_greater = target_pos.y > self.pos.y
            if distance.y > 4 or self.velocity.y < 0:
                self.accelerate(Direction.DOWN if target_greater else Direction.UP)
            else:
                self.accelerate(Direction.UP if target_greater else Direction.DOWN)

    def add_trail_dot(self):
        pos_x = self.pos.x + (ENTITY_SIZE / 2) - 8
        pos_y = self.pos.y + (ENTITY_SIZE / 2) - 8
        self.trail.append(Vector(pos_x, pos_y))

    # pylint: disable=I0011,E1101
    def handle_keys(self, keys):
        if keys[Pygame.K_a] or keys[Pygame.K_LEFT]:
            self.accelerate(Direction.LEFT)
        if keys[Pygame.K_d] or keys[Pygame.K_RIGHT]:
            self.accelerate(Direction.RIGHT)
        if keys[Pygame.K_w] or keys[Pygame.K_UP]:
            self.accelerate(Direction.UP)
        if keys[Pygame.K_s] or keys[Pygame.K_DOWN]:
            self.accelerate(Direction.DOWN)

    def update(self, game):
        self.check_bounds(game.size)
        self.decelerate()
        if self.is_bot:
            self.move_bot(game)
        else:
            self.handle_keys(pygame.key.get_pressed())
        self.move()
        if len(self.trail) == MAX_TRAIL_COUNT:
            self.trail.pop(0)
        self.add_trail_dot()
