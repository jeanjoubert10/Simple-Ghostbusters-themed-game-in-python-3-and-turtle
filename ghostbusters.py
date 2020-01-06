# Silly Ghostbusters themed game in Python 3 and Turtle J Joubert 3 Jan 2020
# Playin with simple gif animation in Turtle
# Create .gif files for free at ezgif.com!!!
# Written in osX and IDLE
# May need speed adjustment in windows (time.sleep)
# sound via os.system(afplay) (aplay in linux)
# use winsound in windows

import turtle
import random
import os
import time


win = turtle.Screen()
win.title('Ghostbusters game')
win.setup(800,600)
win.bgpic('back1.gif')
win.tracer(0)
win.listen()

gif_list = ['slimer1.gif', 'slimer2.gif', 'slimer3.gif', 'beam0.gif', 'beam1.gif',
            'beam2.gif', 'beam3.gif']

for shape in gif_list:
    win.register_shape(shape)

x_speed = [-2, -1.5, -1, 1, 1.5, 2]

slimer = turtle.Turtle()
slimer.s = 'slimer1.gif'
slimer.shape(slimer.s)
slimer.up()
slimer.dx = random.choice(x_speed)
slimer.dy = 2

beam = turtle.Turtle()
beam.s = 'beam0.gif'
beam.shape(beam.s)
beam.up()
beam.goto(0,-150)

pen = turtle.Turtle()
pen.hideturtle()
pen.up()
pen.color('red')
pen.goto(180,250)
pen.write('Score:  0', align='center', font=('Courier', 24, 'normal'))


def move_right():
    if beam.xcor()<= 350:
        beam.goto(beam.xcor()+40, beam.ycor())

def move_left():
    if beam.xcor()>= -350:
        beam.goto(beam.xcor()-40, beam.ycor())


counter = 0
timer = 0
score = 0


def animate_slimer():
    global counter

    if slimer.s == 'slimer1.gif' and counter%10 == 0:
        slimer.s = 'slimer2.gif'
        slimer.shape(slimer.s)
    elif slimer.s == 'slimer2.gif' and counter%10 == 0:
        slimer.s = 'slimer3.gif'
        slimer.shape(slimer.s)
    elif slimer.s == 'slimer3.gif' and counter%10 == 0:
        slimer.s = 'slimer1.gif'
        slimer.shape(slimer.s)


    # Move slimer just like bouncing a ball in pong
    slimer.goto(slimer.xcor()+slimer.dx, slimer.ycor()+slimer.dy)

    if slimer.xcor()<= -360 or slimer.xcor()>= 360:
        slimer.dx *= -1

    if slimer.ycor()>= 260:
        slimer.dy *= -1

    if slimer.ycor()<-300:
        slimer.goto(random.randint(-350,350), 200)
        slimer.dx = random.choice(x_speed)


def shoot_beam(): # When 'space' is pressed - shoot beam
    global timer
    
    if beam.s == 'beam0.gif':
        beam.s = 'beam1.gif'
        beam.shape(beam.s)
        os.system('afplay ray.wav&')
        timer = 0
    
    
def animate_beam():
    global counter

    if beam.s == 'beam1.gif' and counter%10 == 0:
        beam.s = 'beam2.gif'
        beam.shape(beam.s)
    elif beam.s == 'beam2.gif' and counter%10 == 0:
        beam.s = 'beam3.gif'
        beam.shape(beam.s)
    elif beam.s == 'beam3.gif' and counter%10 == 0:
        beam.s = 'beam1.gif'
        beam.shape(beam.s)
        
    if beam.s != 'beam0.gif': # If beam is firing - time limit
        time_check()


def time_check(): # Limit the time the ray is firing
    global timer
    timer += 1
    if timer >100:
        beam.s = 'beam0.gif'
        beam.shape(beam.s)
    
    

win.onkey(move_right, 'Right')
win.onkey(move_left, 'Left')
win.onkey(shoot_beam, 'space')


while True:
    win.update()
    animate_slimer()
    animate_beam()
    counter += 1

    if beam.s == 'beam0.gif':
        beam.goto(beam.xcor(), -230)
    else:
        beam.goto(beam.xcor(), -150)
        

    if slimer.xcor() >= beam.xcor()-100 and slimer.xcor() <= beam.xcor()-50 and beam.s!='beam0.gif':
        if slimer.ycor()<= -70 and slimer.ycor()>=-100:
            slimer.goto(random.randint(-350,350), 200)
            slimer.dx = random.choice(x_speed)
            score += 1
            pen.clear()
            pen.write(f'Score:  {score}', align='center', font=('Courier', 24, 'normal'))

    if slimer.ycor()<-120 and score>0:
        score = 0
        os.system('afplay shout.wav&')
        pen.clear()
        pen.write(f'Score:  {score}', align='center', font=('Courier', 24, 'normal'))
    elif slimer.ycor()<-120 and score == 0:
        os.system('afplay shout.wav&')
            

    time.sleep(0.01) # fps 100 (1/100)







    
