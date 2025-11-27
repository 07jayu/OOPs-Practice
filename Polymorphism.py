class circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
class  rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
    
shapes = [circle(5), rectangle(4, 6), square(4)]

for shape in shapes:
    print("Area:", shape.area())