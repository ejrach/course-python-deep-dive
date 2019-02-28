
class Rectangle:
    def __init__(self, width, height):              
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def to_string(self):
        return "Rectangle: width={0}, height={1}".format(self.width, self.height)

    # if we want to override the string representation of 'str'
    # i.e 'str(r1), then use double underscore
    # this ends up being the same thing as to_string
    def __str__(self):
        return "Rectangle: width={0}, height={1}".format(self.width, self.height)

    def __repr__(self):
        return "Rectangle({0}, {1})".format(self.width, self.height)

    # using dunder equal to compare one object (self), to another (other)
    # If you're trying to compare something other than a rectangle, then we're going to return false
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False

    # implement override for 'less than'
    # This checks if the area of one rectangle is less than the area of another
    def __lt__(self, other):
        if isinstance(other, Rectangle):  # read as "check if other is an instance of Rectangle"
            return self.area() < other.area()
        else:
            return NotImplemented


# create an instance of the class
r1 = Rectangle(10,20)
print(r1.width)
r1.width = 100
print(r1.width)

r1 = Rectangle(10,20)
print(r1.area())
print(r1.perimeter())

# get the address of r1
print(hex(id(r1)))

# these perform the same output. The second print is 
# just overriding 'str'
print(r1.to_string())
print(str(r1))

# Using __repr__ 
print(r1)

r2 = Rectangle(10,20)

# using __eq__ to compare objects to each other
r1 = Rectangle(10,20)
r2 = Rectangle(10,20)

# Object r1 is not r2, prints True
print (r1 is not r2)

# height and width of rectangles are the same, prints True
print(r1 == r2)

# compare r1 to something other than r2, i.e. 100, displays false.
# r1 is not 100
print(r1 == 100)

# using __lt__ to one rectangle area to another
r1 = Rectangle(10,20)
r2 = Rectangle(100,200)
print(r1 < r2)