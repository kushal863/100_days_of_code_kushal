from turtle import Turtle,Screen


tt = Turtle()
screen = Screen()


def move_forword():
    tt.forward(10)
def move_backword():
    tt.backward(10)
def move_left():
    tt.left(10)
def move_right():
    current_heading =tt.heading()-10
    tt.setheading(current_heading)

def cursor_clear():
    tt.clear()
    tt.penup()
    tt.home()

# def counter_clockwise():
#     tt.se

screen.listen()

screen.onkey(key='w',fun=move_forword)

screen.onkey(key='s',fun=move_backword)

screen.onkey(key='a',fun=move_left)
screen.onkey(key='d',fun=move_right)

screen.onkey(key='c',fun=cursor_clear)


screen.exitonclick()