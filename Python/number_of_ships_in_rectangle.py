"""
Split into four quadrants
  only keep checking
  This will give us at most ~398 calls to the hasShip function

"""
class Sea(object):
  def hasShip(self, topright: "Point", bottomleft: "Point") -> bool:
    return 

class Point(object):
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y


def countShips(sea, topright, bottomleft):

  def helper(topright, bottomleft):
    # there may be a crossover so that is our terminal condition
    if bottomleft.x > topright.x or bottomleft.y > topright.y:
      return 0
    # eventually we will get to a singualrity or a point, this will tell us if our quadrant has a ship
    elif bottomleft.x == topright.x and bottomleft.y == topright.y:
      if Sea.hasShip(topright, bottomleft):
        return 1
      else:
        return 0
    
    # if there are no ships then we can return 0 ships
    if not Sea.hasShip(topright, bottomleft):
      return 0

    # divide the rectangle into quadrants with the midpoint
    y_midpoint = (topright.y - bottomleft.y) // 2
    x_midpoint = (topright.x - bottomleft.x) // 2
    midpoint = Point(x_midpoint, y_midpoint)

    # find the ships in each quadrant
    top_left_quadrant = helper(Point(midpoint.x, topright.y), Point(bottomleft.x, midpoint.y + 1))
    top_right_quadrant = helper(topright, Point(midpoint.x + 1, midpoint.y + 1))
    bottom_left_quadrant = helper(midpoint, bottomleft)
    bottom_right_quadrant = helper(Point(topright.x, midpoint.y), Point(midpoint.x + 1, bottomleft.y))

    # return the total ships found in each quadrant
    return top_left_quadrant + top_right_quadrant + bottom_left_quadrant + bottom_right_quadrant

  return helper(topright, bottomleft)
