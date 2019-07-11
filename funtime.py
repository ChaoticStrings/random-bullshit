from sense_hat import SenseHat
from guizero import *
from time import sleep

sense = SenseHat()
x = 0
y = 0

def draw_ball():
    sense.set_pixel(x,y,(183,125,63))

while True:
    sense.clear()
    d = sense.get_accelerometer_raw()['x']
    o = sense.get_accelerometer_raw()['y']
    h = sense.get_accelerometer_raw()['z']
    print(d)
    #d = round(d, 0)
    print("asd : " + str(d))
    #o = round(o, 0)

    if  o < 0:
        sense.set_pixel(x,y, (0,0,0))
        if y > 0:
            y -= 1
    elif o > 0:
        sense.set_pixel(x,y, (0,0,0))
        if y < 7:
            y += 1
    elif d > 0:
        sense.set_pixel(x,y, (0,0,0))
        if x > 0:
            x += 1
    elif d < 0:
        sense.set_pixel(x,y, (0,0,0))
        if x < 7:
            x -= 1    
    draw_ball()
    sleep(0.5)
