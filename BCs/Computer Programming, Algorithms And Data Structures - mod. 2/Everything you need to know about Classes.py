# https://youtu.be/tmY6FEF8f1o

import turtle
class Polygon:

    def __init__(self, sides, name, size = 100, color="black", line_thickness = 3):
        self.sides = sides
        self.name = name
        self.size = size
        self.color = color
        self.line_thickness = line_thickness
        self.interior_angles = (self.sides - 2) * 180
        self.angle = self.interior_angles / self.sides

    def draw(self):
        turtle.color = self.color
        for i in range(self.sides):
            turtle.forward(100)
            turtle.right(180 - self.angle)
        turtle.done()

# Square is a sublcass of Polygon
class Square(Polygon):
    def __init__(self, size = 100, color="black", line_thickness = 3):
        super().__init__(4, "Square", size, color, line_thickness)

square = Square()


#square = Polygon(4, "Square", 200)
#pentagon = Polygon(5, "Pentagon")  # can avoid saying all the time the size because there is the default

#print(square.sides)  # gives 4 as result
#print(square.name)  # gives "Square"

#print(pentagon.sides)  # gives 5 as result
#print(pentagon.name)  # gives "Pentagon"

#square.draw()
#pentagon.draw()

#hexagon = Polygon(6, "Hexagon", 120, "red")
#hexagon.draw()





