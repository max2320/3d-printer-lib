from pin import Pin
import time

DEFAULT_VELOCITY = 5
DEFAULT_WAIT = 0.005
DEFAULT_POSITION_STEP = 1

class Motor:
  def __init__(self, directionIO, stepIO):
    self.directionIO = Pin(directionIO, 'OUT')
    
    self.stepIO = Pin(stepIO, 'OUT')

    self.direction = False
    self.velocity = DEFAULT_VELOCITY
    self.default_wait = DEFAULT_WAIT

    self.position = 0
    self.turn = DEFAULT_POSITION_STEP

  def set_direction(self, direction):
    if direction == "F":
      self.direction = True
    else: 
      self.direction = False
    self.directionIO.set_state(self.direction)


  def step(self, counter, direction):
    self.set_direction(direction)
    self.do_step(counter)

  def do_step(self, counter):
    while counter < 0:
      self.send_step()
      counter -=1

  def send_step(self):
    self.stepIO.send_signal()
    self.wait_time()

  def wait_time(self):
    time.sleep(self.default_wait / self.velocity)

  def next_position(self):
    self.step(self.turn, "F")
    self.position += 1

  def back_position(self):
    self.step(self.turn, "F")
    self.position -= 1

  def move_to(self, destination):
    if destination != self.position 
      if destination > self.position:
        self.next_position()
      else:
        self.back_position()
      self.move_to(self, destination)


class Nozzle(Motor):
  def do_print(self):
    self.step(self.turn, "F")



