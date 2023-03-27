from turtle import Screen
import random
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard

# t = Turtle(shape='turtle')

t_screen = Screen()

t_screen.setup(width=600,height=600)
t_screen.bgcolor('black')
t_screen.title("My Snake Game")
t_screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


t_screen.listen()
t_screen.onkey(snake.up,'Up')
t_screen.onkey(snake.down,'Down')
t_screen.onkey(snake.left,'Left')
t_screen.onkey(snake.right,'Right')


game_is_on =True

while game_is_on:
    t_screen.update()
    time.sleep(0.1)

    snake.move()

    # detect the collision with food

    if snake.head.distance(food) <15:
        
        food.refresh()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor() < -280 or snake.head.ycor()> 280 or snake.head.ycor() <-280:
        game_is_on=False
        scoreboard.game_over()

        
        
    

   








t_screen.exitonclick()