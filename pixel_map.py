class PixelMap:
  def __init__(self, imageMap):
    self.z = len(imageMap)
    print "Z: %s", self.z
    self.x = len(imageMap[0])
    print "X: %s", self.x
    self.y = len(imageMap[0][0])
    print "Y: %s", self.y

    self.tensor = []

    for i in range(0, self.z):
      level = [];

      for i in range(0, self.x):
        row = []
        
        for i in range(0, self.y):
          row.append(imageMap[self.z][self.x][self.y])

        self.tensor.append(row)

      self.tensor.append(level)

  def set_pixel(self, x, y, z, state):
    self.tensor[x][y][z] = state

  def get_pixel(self, x, y, z):
    return self.tensor[x][y][z]
