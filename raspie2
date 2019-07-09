from sense_hat import SenseHat

from time import sleep

sense = SenseHat()

r=(247,86,61)
l=(105,198,247)
g=(132,247,61)
y=(249,247,77)
w=(255,255,255)
c=(183,125,63)
b=(81,61,26)
p=(234,126,173)
a=(2,247,202)
j=(0,0,0)

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
sense.set_pixel(x, y, 255, 255, 255)

def move_up(event):
    global y
    if event.action == 'pressed' and y > 0:
        y -= 1
sense.stick.direction_up = move_up

def move_down(event):
    global y
    if event.action == 'pressed' and y < 8:
        y += 1
sense.stick.direction_down = move_down

def move_left(event):
    global x
    if event.action == 'pressed' and x > 0:
        x -= 1
sense.stick.direction_left = move_left

def move_right(event):
    global x
    if event.action == 'pressed' and x < 8:
        x += 1
sense.stick.direction_right = move_right

def draw_ball():
    sense.set_pixel(x, y, 183, 125, 63)
    
ball_position = [x, y]

if ball_position[0] == [7,7] or ball_position[0] == [6,7]:
   sense.clear()	
   sense.show_message("Bath time!", scroll_speed=0.05, text_colour=[105, 198, 247])
bath = True
while True:
	    last_angle == angle
	    while angle == last_angle:
		angle = choice([0, 90, 180, 270])
	    sense.set_rotation(angle)
	    sense.set_pixels(arrow)
	    sleep(pause)
            acceleration = sense.get_accelerometer_raw()
            x = acceleration['x']
            y = acceleration['y']
            z = acceleration['z']

            x = round(x, 0)
            y = round(y, 0)

	    if x == 1 and y == 1:
   	         sense.set_pixel(0,0, 255,255,255)

def draw_ball():
    sense.set_pixel(x, y, 183, 125, 63)

    
while True:
    sense.clear(0, 0, 0)
    draw_ball()
    sleep(0.25)
