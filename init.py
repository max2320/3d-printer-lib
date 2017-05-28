from printer import Printer

# Motor(direction, step)

motorX=['CSID0','CSID1']
motorY=['CSID2','CSID3']
motorZ=['CSID4','CSID5']
nozzle=['CSID6','CSID7']


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
print(printerOBJ.nozzle)
printerOBJ.print_level(0);

