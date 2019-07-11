from sense_hat import SenseHat
from guizero import *
from time import sleep

sense = SenseHat()


def draw_ball():
    sense.set_pixel(x,y,(183,125,63))

while True:
    d = sense.get_accelerometer_raw()['x']
    o = sense.get_accelerometer_raw()['y']
    h = sense.get_accelerometer_raw()['z']
    x = 0
    y = 0
    d = round(x, 0)
    o = round(y, 0)

    if  o == -1:
        sense.set_pixel(x,y, (0,0,0))
        if o > 0:
            y -= 1
    elif o == 1:
        sense.set_pixel(x,y, (0,0,0))
        if o < 7:
            y += 1
    elif d == 1:
        sense.set_pixel(x,y, (0,0,0))
        if d > 0:
            x -= 1
    elif d == -1:
        sense.set_pixel(x,y, (0,0,0))
        if d < 7:
            x += 1    
    draw_ball()
