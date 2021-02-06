from pyfirmata import Arduino, OUTPUT
import time

board=Arduino('COM6')
verm = 7
amar = 6
verd = 5

board.digital[verm].mode = OUTPUT
board.digital[amar].mode = OUTPUT
board.digital[verd].mode = OUTPUT

while True:
    board.digital[verm].write(1)
    time.sleep(5)
    board.digital[verm].write(0)
    board.digital[amar].write(1)
    time.sleep(3)
    board.digital[amar].write(0)
    board.digital[verd].write(1)
    time.sleep(5)
    board.digital[verd].write(0)