from turtle import Turtle,Screen

tt = Turtle()

tt.shape('arrow')
tt.shapesize(1)
tt_screen = Screen()

for _ in range(20):
    tt.forward(10)
    tt.penup()
    tt.forward(10)
    tt.pendown()

tt_screen.exitonclick()