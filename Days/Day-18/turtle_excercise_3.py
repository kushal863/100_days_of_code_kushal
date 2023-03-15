from turtle import Turtle,Screen
import random

tt = Turtle()
colors =[  "black", "red", "green", "blue", "cyan", "yellow","magenta","green", "blue", "cyan"]

tt.shape('arrow')
tt_screen = Screen()

def draw_shale(sides):
    angle = 360//sides
    for _ in range(sides):
        tt.forward(100)
        tt.right(angle)

for i in range(3,10):
    draw_shale(i)
    
    tt.pencolor(random.choice(colors))
    # print(360//i)


tt_screen.exitonclick()