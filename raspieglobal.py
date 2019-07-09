from sense_hat import SenseHat
from guizero import *
from time import sleep

sense = SenseHat()

r=(247,86,61)
l=(105,198,247)
g=(132,247,61)
t=(249,247,77)
w=(255,255,255)
c=(183,125,63)
b=(81,61,26)
p=(234,126,173)
a=(2,247,202)
j=(0,0,0)
z=(86,86,30)

image= [
j,j,j,j,j,j,j,j,
c,c,j,j,j,j,c,c,
c,p,c,c,c,c,p,c,
j,c,a,c,c,a,c,j,
j,c,c,c,c,c,c,j,
j,c,c,b,b,c,c,j,
j,j,c,b,b,c,j,j,
j,j,j,j,j,j,j,j
]
sense.set_pixels(image)
sleep(1)

sense.show_message("Raspie!", scroll_speed=0.05, text_colour=[183,125,63])
y = 4
x = 4
def draw_ball():
            sense.set_pixel(0,7,(132,247,61))
            sense.set_pixel(1,7,(132,247,61))
            sense.set_pixel(2,7,(234,126,173))
            sense.set_pixel(3,7,(234,126,173))
            sense.set_pixel(4,7,(247,86,61))
            sense.set_pixel(5,7,(247,86,61))
            sense.set_pixel(6,7,(105,198,247))
            sense.set_pixel(7,7,(105,198,247))
            sense.set_pixel(3,0,(255,255,255))
            sense.set_pixel(4,0,(255,255,255))
            sense.set_pixel(x,y,(183,125,63))

while True:
    global state
    state = "menu"
    if state == "menu":
        def move_up(event):
            global y
            sense.set_pixel(x,y, (0,0,0))
            if event.action == 'pressed' and y > 0:
                y -= 1
        sense.stick.direction_up = move_up
        def move_down(event):
            global y
            sense.set_pixel(x,y, (0,0,0))
            if event.action == 'pressed' and y < 7:
                y += 1
        sense.stick.direction_down = move_down
        def move_left(event):
            global x
            sense.set_pixel(x,y, (0,0,0))
            if event.action == 'pressed' and x > 0:
                x -= 1
        sense.stick.direction_left = move_left
        def move_right(event):
            global x
            sense.set_pixel(x,y, (0,0,0))
            if event.action == 'pressed' and x < 7:
                x += 1
        sense.stick.direction_right = move_right
        draw_ball()


    if x == 2 and y == 7 and state == "menu":
        state = "sleep"

    def move_middle(event):
        global light
        if event.action == 'pressed':
            sense.set_pixels(lights_off)

    if state == "sleep":
        lights_on= [
        j,j,j,j,j,j,t,c,
        j,j,j,j,j,j,t,t,
        j,j,j,j,j,j,j,j,
        j,c,c,j,j,j,j,c,
        j,c,c,c,c,c,c,j,
        r,w,c,c,c,c,w,r,
        r,w,w,w,w,w,w,r,
        r,r,r,r,r,r,r,r
        ]

        lights_off=[
        j,j,j,j,j,j,z,c,
        j,j,j,j,j,j,z,z,
        j,j,j,j,j,j,j,j,
        j,j,j,j,j,j,j,j,
        j,j,j,j,j,j,j,j,
        j,j,j,j,j,j,j,j,
        j,j,j,j,j,j,j,j,
        j,j,j,j,j,j,j,j
        ]
        sense.set_pixels(lights_on)
        sense.stick.direction_middle = move_middle
        sleep(10)
        sense.clear(0,0,0)
        state = "menu"       



