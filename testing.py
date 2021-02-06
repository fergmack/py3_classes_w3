# As an example, suppose you want to find the distance between two points, given by the coordinates (x1, y1) and (x2, y2).

# Obviously, this version of the function doesn’t compute distances; it always returns None. But it is syntactically correct, and it will run, which means that we can test it before we make it more complicated.

# The distance between any point and itself should be 0.

def distance(x1, y1, x2, y2):
  dx = x2 - x1 
  dy = y2 - y1 
  dsquared = dx**2 + dy**2
  # get square root 
  result = dsquared ** 0.5
  return result

# tests 
assert distance(1, 2, 1, 2) == 0 
assert distance(1, 2, 4, 6) == 5
assert distance (0, 0, 1, 1 ) == 2**0.5

# --------- Testing Classes ------------------
# To test whether the class constructor (the __init__) method is working correctly, create an instance and then make tests to see whether its instance variables are set correctly. Note that this is a side effect test: the constructor method’s job is to set instance variables, which is a side effect. Its return value doesn’t matter.

class Point:
  '''move x, y coordinates'''

  def __init__(self, initX, initY):
    self.x = initX
    self.y = initY 

  def distanceFromOrigin(self):
    return ( (self.x **2) + (self.y **2 )) ** 0.5

  def move(self, dx, dy):
    self.x = self.x + dx 
    self.y = self.y + dy 

# testing the class constructor 
p = Point(3, 4)
assert p.y == 4
assert p.x == 3 

# testing the distance method 
p = Point(3, 4)
assert p.distanceFromOrigin() == 5.0

# testing the move method 
p = Point(3, 4)
p.move(-2, 3)
assert p.x == 1 
assert p.y == 7
if p.y == 7:
  print('y passed')
