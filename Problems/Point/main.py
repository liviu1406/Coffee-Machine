class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, class_):
        return ((self.x - class_.x) ** 2 + (self.y - class_.y) ** 2) ** 0.5
