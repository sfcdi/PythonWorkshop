# Class describes a wall
class Wall:

    # initialize the class
    def __init__(self, height, length):
        self.Height = height
        self.Length = length

    # returns the area
    def Area(self):
        area = self.Height * self.Length
        return area

    # Shortens the wall
    def SubtractLength(self, x):
        self.Length -= x
        print(self.Length)
		
# let's try using the wall
w = Wall(5, 6)

print(w.Height)
print(w.Length)
print(w.Area())

# let's try changing the height
w.Height = 10
print(w.Height)

# use the subtract length method
w.SubtractLength(2)
print(w.Length)
print(w.Area())


