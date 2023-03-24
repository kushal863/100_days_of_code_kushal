from turtle import Turtle, Screen
import random
import time

from snake import Snake

# t = Turtle(shape='turtle')

t_screen = Screen()

t_screen.setup(width=600,height=600)
t_screen.bgcolor('black')
t_screen.title("My Snake Game")
t_screen.tracer(0)


snake = Snake()




game_is_on =True

while game_is_on:
    t_screen.update()
    time.sleep(0.1)

    snake.move()







t_screen.exitonclick()