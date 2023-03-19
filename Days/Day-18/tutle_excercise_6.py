import turtle as t
import random

tt = t.Turtle()

t.colormode(255)
tt.shape('arrow')
tt_screen = t.Screen()
angle = [90,0,180,270]
tt.speed('fastest')


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
def draw_spiralgraph(size_of_gap):
    for _ in range(360//size_of_gap):
        tt.circle(100)
        tt.color(random_color())
        current_heading=tt.heading()
        tt.setheading(current_heading+size_of_gap)

draw_spiralgraph(5)

tt_screen.exitonclick()