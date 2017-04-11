import math
from random import randint

# pylint: disable=I0011,invalid-name
class Vector(object):
    def __init__(self, x, y=None):
        self.x = x
        if y is None:
            self.y = x
        else:
            self.y = y

    def get_distance(self, other):
        distance = self.get_distance_components(other)
        return math.sqrt(pow(distance.x, 2) + pow(distance.y, 2))

    def get_distance_components(self, other):
        return Vector(abs(self.x - other.x), abs(self.y - other.y))

    def add(self, other):
        return self._calc(other, lambda a, b: a + b)

    def sub(self, other):
        return self._calc(other, lambda a, b: a - b)

    def mul(self, other):
        return self._calc(other, lambda a, b: a * b)

    def div(self, other):
        return self._calc(other, lambda a, b: a / b)

    def _calc(self, other, func):
        if isinstance(other, Vector):
            return Vector(func(self.x, other.x), func(self.y, other.y))
        else:
            return Vector(func(self.x, other), func(self.y, other))

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def slow(self, diff):
        self.x = Vector._slow(diff, self.x)
        self.y = Vector._slow(diff, self.y)

    @staticmethod
    def _slow(diff, num):
        if num == 0:
            return 0
        if num > 0:
            return num - diff
        else:
            return num + diff

    @staticmethod
    def rand(min_v, max_v):
        x = randint(min_v.x, max_v.x)
        y = randint(min_v.y, max_v.y)
        return Vector(x, y)

class TimeVector(Vector):
    def __init__(self, x, y, time):
        super().__init__(x, y)
        self.time = time
