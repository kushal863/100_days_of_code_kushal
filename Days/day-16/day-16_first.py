"""
The turtle library in Python is a built-in graphics library
 that allows you to create and control a turtle object on a canvas.
   The turtle object can be moved around the canvas,
     and its movements can be customized using various commands
       such as forward, backward, left, right, penup, pendown, etc.
         The turtle library is often used for teaching programming 
         concepts to beginners, as it provides a fun and interactive way to learn
           about variables, loops, and conditional statements.


"""

from turtle import Turtle, Screen
import another_module

print(another_module.another_variable)

timmy=Turtle()
timmy.color('red')

timmy.forward(100)
screen =Screen()


print(timmy)
print(screen.canvheight)



screen.exitonclick()