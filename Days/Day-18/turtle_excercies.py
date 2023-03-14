from turtle import Turtle,Screen

tt = Turtle()

tt.shape('arrow')
tt_screen = Screen()


for _ in range(4):
    tt.forward(100)
    tt.left(90)

tt_screen.exitonclick()