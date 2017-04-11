import time
from lib.constants import ACCEL_SPEED, Direction
from lib.Vector import Vector

class Rectangle(object):
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.creation_time = time.time()

    def collides(self, other):
        return ((
            self.pos.x <= other.pos.x + other.size.x
        ) and (
            other.pos.x <= self.pos.x + self.size.x
        )) and ((
            self.pos.y <= other.pos.y + other.size.y
        ) and (
            other.pos.y <= self.pos.y + self.size.y
        ))

    def get_distance(self, other):
        return self.pos.get_distance(other.pos)

    def get_distance_components(self, other):
        return self.pos.get_distance_components(other.pos)

class AccelRectangle(Rectangle):
    def __init__(self, pos, size):
        super().__init__(pos, size)
        self.velocity = Vector(0)

    def accelerate(self, direction):
        if direction == Direction.UP:
            self.velocity.y -= ACCEL_SPEED
        elif direction == Direction.DOWN:
            self.velocity.y += ACCEL_SPEED
        elif direction == Direction.LEFT:
            self.velocity.x -= ACCEL_SPEED
        elif direction == Direction.RIGHT:
            self.velocity.x += ACCEL_SPEED

    def check_bounds(self, bounds):
        if self.pos.x < 0:
            self.pos.x = 0
            if self.velocity.x < 0:
                self.velocity.x = 0
        elif self.pos.x > bounds.x - self.size.x:
            self.pos.x = bounds.x - self.size.x
            if self.velocity.x > 0:
                self.velocity.x = 0
        if self.pos.y < 0:
            self.pos.y = 0
            if self.velocity.y < 0:
                self.velocity.y = 0
        elif self.pos.y > bounds.y - self.size.y:
            self.pos.y = bounds.y - self.size.y
            if self.velocity.y > 0:
                self.velocity.y = 0

    def decelerate(self):
        self.velocity.slow(ACCEL_SPEED / 2)

    def move(self):
        self.pos.x += self.velocity.x
        self.pos.y += self.velocity.y
