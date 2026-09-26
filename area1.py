class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self):
        return self.x*self.y

class circle(shape):
    def __init__(self,radius):
        super().__init__(self,radius)
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius
rec = shape(4,5)
print(rec.area())

cir = circle(22)
print(cir.area())