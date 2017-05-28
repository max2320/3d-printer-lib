import CHIP_IO.GPIO as GPIO

class Pin:
  def __init__(self, label, mode = 'OUT'):
    self.state = False
    self.label = label
    print mode
    self.set_mode(mode)


  def set_mode(mode):
    if mode == "IN":
      GPIO.setup(self.label, GPIO.IN)
    else:
      GPIO.setup(self.label, GPIO.OUT)

  def send_signal():
    self.set_state(True)
    self.set_state(False)

  def set_state(state):
    self.state = state

    if state == True:
      GPIO.output(self.label, GPIO.HIGH)
    else:
      GPIO.output(self.label, GPIO.LOW)

  def get_state():
    return GPIO.input(self.label)    