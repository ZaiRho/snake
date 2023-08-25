from turtle import Turtle, Screen
import turtle
import time

class Snake:
    def __int__(self):
        self.snakes = []
        sesnake_length = 10
        start_posx = 0
        start_posy = 0


turtle.delay(0)

previous_position =(0,0)
previous_heading = 0
new_position =(0,0)
new_heading = 0


for i in range(snake_length):
    new_player = Turtle(shape="square")
    new_player.penup()
    new_player.color("coral")
    new_player.setx(start_posx)
    new_player.sety(start_posy)
    # new_player.speed("fastest")
    if new_player.heading() == 0:
        start_posx -= 20
    elif new_player.heading() == 90:
        start_posy -= 20
    elif new_player.heading() == 180:
        start_posx += 20
    elif new_player.heading() == 360:
        start_posy += 20
    snakes.append(new_player)


def forward():
    global new_position
    global new_heading
    new_position = snakes[0].pos()
    new_heading = snakes[0].heading()
    snakes[0].forward(20)
    update()
    print("forward")



def bind_a():
    global new_position
    global new_heading
    new_position = snakes[0].pos()
    new_heading = snakes[0].heading()
    snakes[0].seth(180)
    update()



def bind_d():
    global new_position
    global new_heading
    new_position = snakes[0].pos()
    new_heading = snakes[0].heading()
    snakes[0].seth(0)
    update()


def bind_w():
    global new_position
    global new_heading
    new_position = snakes[0].pos()
    new_heading = snakes[0].heading()
    snakes[0].seth(90)
    update()


def bind_s():
    global new_position
    global new_heading
    new_position = snakes[0].pos()
    new_heading = snakes[0].heading()
    update()
    snakes[0].seth(270)


def update():
    global new_position
    global new_heading
    global previous_heading
    global previous_position
    for k in range(1, len(snakes)):
        previous_position = snakes[k].pos()
        previous_heading = snakes[k].heading()
        snakes[k].setpos(new_position)
        snakes[k].seth(new_heading)
        new_heading = previous_heading
        new_position = previous_position


screen = Screen()
screen.tracer(0)
screen.onkey(bind_w, "w")
screen.onkey(bind_d, "d")
screen.onkey(bind_a, "a")
screen.onkey(bind_s, "s")
screen.exitonclick()

while True:
    forward()
    screen.update()
    time.sleep(0.5)
    screen.listen()

# i was trying to test github commit








