from turtle import Turtle,Screen
import random

tt = Turtle()
colors =["black", "red", "green", "blue", "cyan", "yellow","magenta","green", "blue", "cyan"]

tt.shape('arrow')
tt_screen = Screen()
angle = [90,0,180,270]
tt.pensize(15)
tt.speed('fastest')
for _ in  range(100):
    
    tt.forward(35)
    tt.pencolor(random.choice(colors))
    tt.setheading(random.choice(angle))


tt_screen.exitonclick()