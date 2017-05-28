class PixelMap:
  def __init__(self, imageMap):
    self.Z = len(imageMap) -1
    self.X = len(imageMap[0]) -1
    self.Y = len(imageMap[0][0]) -1
    print "Z: %s", self.Z
    print "X: %s", self.X
    print "Y: %s", self.Y

    self.tensor = imageMap

  def set_pixel(self, x, y, z, state):
    print '%s, %s, %s, %s', x, y, z, state
    self.tensor[z][x][y] = state

  def get_pixel(self, x, y, z):
    print '%s, %s, %s', x, y, z

    return self.tensor[z][x][y] == 1

