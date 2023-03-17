import turtle as t
import random

tt = t.Turtle()

t.colormode(255)
tt.shape('arrow')
tt_screen = t.Screen()
angle = [90,0,180,270]
tt.pensize(15)
tt.speed('fastest')


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

print(random_color())
for _ in  range(100):
    
    tt.forward(35)
    tt.pencolor(random_color())
    tt.setheading(random.choice(angle))


tt_screen.exitonclick()