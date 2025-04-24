## Polymorphism== to have manny faces
##                poly == many
##               Morphe== form
## 2 types : 1. Inheritance
 #            2.Duck typing


print('######## Inheritance ##################')


class Shape:

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side**2

class Triangle(Shape):
    def __init__(self,base,height):
        self.height=height
        self.base=base

    def area(self):
        return 0.5* self.height*self.base



class Pizza(Circle):
    def __init__(self,topping,radius):
        super().__init__(radius)##################
        self.topping=topping


shapes=[Circle(4),Square(5),Triangle(6,7),Pizza('Peperonni',15)]

for shape in shapes:
    print(shape.area())


##################################################
