class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, alter):
        if self.x == alter.x and self.y == alter.y:
            return True
        else:
            return False
    def __str__(self):
        return f"[{self.x}, {self.y}]"
    def euclidian_distance(self, alter):
        return ((alter.x - self.x)**2 + (alter.y - self.y)**2) ** (1/2)

class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
    def __str__(self):
        return f"x: {self.x} & y: {self.y}"
    def __add__(self,alter):
        new_x = self.x + alter.x
        new_y = self.y + alter.y
        new_vec = Vector(new_x, new_y)
        return new_vec

point1 = Point(5,6)
point2 = Point(8,1)
vec1 = Vector(4,7)
vec2 = Vector(10,20)

a = point1.__eq__(point2)
b = point2.__str__()
c = vec1.__add__(vec2)
d = vec2.__str__()

print(a)
print(b)
print(c)
print(d)