class PixelMap:
  def __init__(self, imageMap):
    self.Z = len(imageMap)
    self.X = len(imageMap[0])
    self.Y = len(imageMap[0][0])
    print "Z: %s", self.Z
    print "X: %s", self.X
    print "Y: %s", self.Y

    self.tensor = imageMap
    
  def set_pixel(self, x, y, z, state):
    self.tensor[x][y][z] = state

  def get_pixel(self, x, y, z):
    return self.tensor[x][y][z] == 1

