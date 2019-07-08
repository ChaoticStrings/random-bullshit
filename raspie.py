from sense_hat import SenseHat
from guizero import *
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

image = [
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

 image = [
j,j,j,j,j,j,j,j,
j,j,j,j,j,j,j,j,
j,j,j,j,j,j,j,j,
j,j,j,j,j,j,j,j,
j,j,j,j,j,j,j,j,
j,j,j,j,j,j,j,j,
j,j,j,j,j,j,j,j,
p,j,j,j,j,j,j,p
]

