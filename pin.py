import CHIP_IO.GPIO as GPIO

class Pin:
  def __init__(self, label, flux = 'OUT'):
    self.state = False
    self.label = label

    self.set_flux(flux)

  def set_flux(flux):
    if flux == "IN":
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