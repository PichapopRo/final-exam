import turtle
import random


class Polygon:
    def __init__(self, num_sides, size, orientation, location, border_size):
        # num_sides, size, orientation, location, color, border_size
        self.num_sides = num_sides  # triangle, square, or pentagon
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = self.get_new_color()
        self.border_size = border_size

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

    def get_new_color(self):
        self.color = (
            random.randint(0, 255), random.randint(0, 255),
            random.randint(0, 255))

    turtle.speed(0)
    turtle.bgcolor('black')
    turtle.tracer(0)
    turtle.colormode(255)

# draw a polygon at a random location, orientation, color, and border line thickness
number = int(input('Which art do you want to generate? Enter a number between 1 to 8,inclusive: '))
if number == 1:
    size = random.randint(50, 150)
    orientation = random.randint(0, 90)
    location = [random.randint(-300, 300), random.randint(-200, 200)]
    border_size = random.randint(1, 10)
    polygon = Polygon(3, size, orientation, location, border_size)
    reduction_ratio = 0.618
if number == 2:
    size = random.randint(50, 150)
    orientation = random.randint(0, 90)
    location = [random.randint(-300, 300), random.randint(-200, 200)]
    border_size = random.randint(1, 10)
    polygon = Polygon(4, size, orientation, location, border_size)
    reduction_ratio = 0.618
if number == 3:
    size = random.randint(50, 150)
    orientation = random.randint(0, 90)
    location = [random.randint(-300, 300), random.randint(-200, 200)]
    border_size = random.randint(1, 10)
    polygon = Polygon(5, size, orientation, location, border_size)
    reduction_ratio = 0.618


# reposition the turtle and get a new location
turtle.penup()
turtle.forward(size*(1-reduction_ratio)/2)
turtle.left(90)
turtle.forward(size*(1-reduction_ratio)/2)
turtle.right(90)
location[0] = turtle.pos()[0]
location[1] = turtle.pos()[1]



# adjust the size according to the reduction ratio
