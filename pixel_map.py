class PixelMap:
  def __init__(self, imageMap):
    self.z = len(imageMap)
    self.x = len(imageMap[0])
    self.y = len(imageMap[0][0])
    print "Z: %s", self.z
    print "X: %s", self.x
    print "Y: %s", self.y

    self.tensor = []

    for z in range(0, self.z):
      level = [];

      for x in range(0, self.x):
        row = []
        
        for y in range(0, self.y):
          row.append(imageMap[z][x][y])

        self.tensor.append(row)

      self.tensor.append(level)

  def set_pixel(self, x, y, z, state):
    self.tensor[x][y][z] = state

  def get_pixel(self, x, y, z):
    return self.tensor[x][y][z]
