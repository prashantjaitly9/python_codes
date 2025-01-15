class Circle():
    def __init__(self, radius):
        self.radius = radius
    
    def Area(self):
        return (3.14 * self.radius * self.radius)
    
    def Perimeter(self):
        return (2 * 3.14 * self.radius)
    
    def show(self):
        print("The radius, circumference, and area of the given circle are: ", self.radius)
        print(self.Area())
        print(self.Perimeter())
    
c1 = Circle(4)
c1.show()

