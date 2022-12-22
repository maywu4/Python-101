import math

# Quadrilateral with Inheritance
# Implement a class called Quadrilateral with a constructor method that initializes two instance properties: length and width.

# Implement a second class called Square that inherits from Quadrilateral.

# Create a constructor method in the Square class that initializes two instance properties length and width -- only if the two values passed into the constructor are equal.

# If the two values are not equal, raise an Exception with the message "A square must have an equal length and width."

# If the values are equal, use the super() function to initialize the same two instance properties from the Quadrilateral class's constructor method.

class Quadrilateral:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Quadrilateral):
    def __init__(self, length, width):
        if length == width:
            super().__init__(length, width)
        else:
            raise Exception('A square must have an equal length and width.')



quad = Quadrilateral(20, 10)
# print(f"{quad.length}, {quad.width}") # 20, 10

square = Square(10, 10)
# print(f"{square.length}, {square.width}") # 10, 10

# not_square = Square(5, 10) # Exception: A square must have an equal length and width.


# Triangle with Inheritance
# Build off your RegularPolygon class and create another class called Triangle. The Triangle class should have functionality that calculates both the perimeter and the area of the triangle. The calculated values for both the perimeter and area should be assigned to respective instance properties on the Triangle class.

# The area of a triangle can be calculated with Heron's formula: √(s(s-a)(s-b)(s-c)), where s is the semi-perimeter of the triangle. The semi-perimeter is the perimeter divided by 2. The square root function sqrt() can be imported from the built-in math package.

# Write your class here.

class Triangle:
    def __init__(self, sides, side_length):
        if not (sides == 3):
            raise Exception('A triangle must have exactly three sides')
        else: 
            self.sides = sides
            self.side_length = side_length

    @property
    def perimeter(self):
        return (self.sides * self.side_length)

    @property
    def area(self):
        s = self.perimeter / 2
        return math.sqrt(s*(s-self.side_length)*(s-self.side_length)*(s-self.side_length))




triangle_a = Triangle(3, 3)
print(triangle_a.perimeter) # 9
print(triangle_a.area) # 3.8971...

triangle_b = Triangle(3, 12)
print(triangle_b.perimeter) # 36
print(triangle_b.area) # 62.3538...

triangle_c = Triangle(4, 12)
# print(triangle_c.perimeter) # Exception: A triangle must have exactly three sides

