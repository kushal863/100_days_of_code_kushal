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


t_screen.listen()
t_screen.onkey(snake.up,'Up')
t_screen.onkey(snake.down,'Down')
t_screen.onkey(snake.left,'Left')
t_screen.onkey(snake.right,'Right')


game_is_on =True

while game_is_on:
    t_screen.update()
    time.sleep(0.3)
    
    
    
    
    

    snake.move()
    

   








t_screen.exitonclick()