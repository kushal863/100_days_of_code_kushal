from turtle import Turtle, Screen
import random
import time

# t = Turtle(shape='turtle')

t_screen = Screen()

t_screen.setup(width=600,height=600)
t_screen.bgcolor('black')
t_screen.title("My Snake Game")
t_screen.tracer(0)

starting_positions = [(0,0),(-20,0),(-40,0)]

segments =[]
for possition in starting_positions:

    segment =Turtle(shape='square')
    segment.penup()
    segment.color('White')
    segment.goto(possition)
    segments.append(segment)



game_is_on =True

while game_is_on:
    
    t_screen.update()
    time.sleep(0.1)
    for seg in range(2,0,-1):
        x_new = segments[seg-1].xcor()
        y_new = segments[seg-1].ycor()
        segments[seg].goto(x_new,y_new)
    # segments[0].forward(20)
        

# segment_1.forward(10)
# segment_2.forward(10)
# segment_3.forward(10)






t_screen.exitonclick()