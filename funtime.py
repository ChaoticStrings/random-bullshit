from sense_hat import SenseHat
from guizero import *
from time import sleep

sense = SenseHat()

while True:
    d = sense.get_accelerometer_raw()['x']
    o = sense.get_accelerometer_raw()['y']
    h = sense.get_accelerometer_raw()['z']

y = 0
x = 0

    d = round(x, 0)
    o = round(y, 0)

    if  o== -1:
          y -= 1
    elif o == 1:
         y += 1
    elif d == 1:
        x +=  1
    elif d == -1
        x -= 1





def draw_ball():
            sense.set_pixel(x,y,(183,125,63))
            sense.set_pixel(6,6(249,247,77))

    if  == -1: