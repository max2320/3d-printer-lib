from printer import Printer
import CHIP_IO.GPIO as GPIO

GPIO.cleanup()

# Motor(direction, step)

motorX=['CSID3', 'CSID2']
motorY=['CSID1', 'CSID0']
motorZ=['CSID5', 'CSID4']
nozzle=['CSID7', 'CSID6']

image = [
  [
    [0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
  ]
]


printerOBJ = Printer(motorX, motorY, motorZ, nozzle, image);

printerOBJ.print_level(0);
