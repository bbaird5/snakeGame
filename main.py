import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title('My Snake Game')

x_coordinates = [0, -20, -40]
segments = []

for i in range(0, 3):
    tim = Turtle(shape='square')
    tim.color('white')
    tim.penup()
    tim.goto(x=x_coordinates[i], y=0)
    segments.append(tim)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)




screen.exitonclick()