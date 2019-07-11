from sense_hat import SenseHat
from guizero import *
from time import sleep

sense = SenseHat()

while True:
    d = sense.get_accelerometer_raw()['x']
    o = sense.get_accelerometer_raw()['y']
    h = sense.get_accelerometer_raw()['z']

    x = 0
    y = 0

    d = round(x, 0)
    o = round(y, 0)

    if  o == -1:
        def move_up(event):
            global y
            sense.set_pixel(x,y, (0,0,0))
            if event.action == 'pressed' and y > 0:
                y -= 1
        sense.stick.direction_up = move_up
    elif o == 1:
        def move_down(event):
            global y
            sense.set_pixel(x,y, (0,0,0))
            if event.action == 'pressed' and y < 7:
                y += 1
        sense.stick.direction_down = move_down
    elif d == 1:
        def move_left(event):
            global x
            sense.set_pixel(x,y, (0,0,0))
            if event.action == 'pressed' and x > 0:
                x -= 1
        sense.stick.direction_left = move_left
    elif d == -1:
       def move_right(event):
            global x
            sense.set_pixel(x,y, (0,0,0))
            if event.action == 'pressed' and x < 7:
                x += 1
        sense.stick.direction_right = move_right        
    draw_ball()

def draw_ball():
            sense.set_pixel(x,y,(183,125,63))
