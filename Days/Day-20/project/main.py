from turtle import Turtle, Screen
import random

# t = Turtle(shape='turtle')

t_screen = Screen()

t_screen.setup(width=600,height=600)
t_screen.bgcolor('black')
t_screen.title("My Snake Game")

segment_1 =Turtle(shape='square')
segment_1.color('White')

segment_2 =Turtle(shape='square')
segment_2.color('White')
segment_2.goto(x=-20,y=0)

segment_3 =Turtle(shape='square')
segment_3.color('White')
segment_3.goto(x=-40,y=0)






t_screen.exitonclick()