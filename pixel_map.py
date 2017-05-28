class PixelMap:
  def __init__(self, imageMap):
    self.Z = len(imageMap)
    self.X = len(imageMap[0])
    self.Y = len(imageMap[0][0])
    print "Z: %s", self.Z
    print "X: %s", self.X
    print "Y: %s", self.Y

    self.tensor = []

    for z in range(0, self.Z):
      level = [];

      for x in range(0, self.X):
        row = []
        
        for y in range(0, self.Y):
          row.append(imageMap[z][x][y])

        self.tensor.append(row)

      self.tensor.append(level)

  def set_pixel(self, x, y, z, state):
    self.tensor[x][y][z] = state

  def get_pixel(self, x, y, z):
    return self.tensor[x][y][z]
