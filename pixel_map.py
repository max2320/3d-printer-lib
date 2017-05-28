class PixelMap:
  def init(self, imageMap):
    self.Z = len(imageMap)
    self.X = len(imageMap[0])
    self.Y = len(imageMap[0][0])


    self.tensor = []

    for i in range(0, Z):
      level = [];

      for i in range(0, X):
        row = []
        
        for i in range(0, Y):
          row.append(imageMap[Z][X][Y])

        self.tensor.append(row)

      self.tensor.append(level)

  def set_pixel(self, x, y, z, state):
    self.tensor[x][y][z] = state

  def get_pixel(self, x, y, z):
    return self.tensor[x][y][z]
