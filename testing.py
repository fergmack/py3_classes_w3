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
