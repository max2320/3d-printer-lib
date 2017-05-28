from pixel_map import PixelMap
from motor import Motor, Nozzle

class Printer:
  def __init__(self, motorX, motorY, motorZ, nozzle, imageMap):
    self.motor_X = Motor(motorX[0], motorX[1])
    self.motor_Y = Motor(motorX[0], motorX[1])
    self.motor_Z = Motor(motorZ[0], motorZ[1])
    self.nozzle = Nozzle(nozzle[0], nozzle[1])
    self.image = PixelMap(imageMap)
  
  def print_level(self, z):
    for x in range(0, self.image.X):
      self.motor_X.move_to(x)
      
      for y in range(0, self.image.Y):
        self.motor_Y.move_to(x)
      
        if self.image.get_pixel(x, y, z) : 
          self.nozzle.do_print()
        
  def print_levels(self):
    for z in range(0, self.image.Z):
      self.print_level(z)

