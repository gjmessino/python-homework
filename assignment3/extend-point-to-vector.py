class Point:
    def __innit__(self, x, y):
        self.x = x
        self.y = y
    def equality(self, alter):
        if self.x == alter.x and self.y == alter.y:
            return True
    def string_representation(self):
        return f"[{self.x}, {self.y}]"
    def euclidian_distance(self, alter):
        return ((alter.x - self.x)**2 + (alter.y - self.y)**2) ** (1/2)

class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y) 
    def string_representation(self):
        return f"{self.x} & {self.y}"