import math

class AreaCalculator:

    def area_square(self, side):
        area = side * side
        return area

    def area_circle(self, radius):
        area = math.pi * radius * radius
        return area

    def area_triangle(self, base, height):
        area = 0.5 * base * height
        return area

    def area_rectangle(self, length, width):
        area = length * width
        return area


# Creating object of the class
calc = AreaCalculator()

# Calling functions
print("Area of Square:", calc.area_square(4))
print("Area of Circle:", calc.area_circle(3))
print("Area of Triangle:", calc.area_triangle(5, 6))
print("Area of Rectangle:", calc.area_rectangle(7, 4))