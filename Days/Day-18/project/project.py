import colorgram
import random
import turtle as t

tt_screen = t.Screen()

# color = colorgram.extract('image.jpg',10)
tt = t.Turtle()
t.colormode(255)
tt.speed('fastest')
tt.penup()
# rgb_colors = []
# for col in color:
#     r = col.rgb.r
#     g = col.rgb.g
#     b = col.rgb.b
#     rgb_colors.append((r,g,b))

# print(rgb_colors)



color_list = [(207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203)]
tt.setheading(255)
tt.forward(300)
tt.setheading(0)
tt.shape('circle')


number_of_dots =100
for dot_count in range(1,number_of_dots):
    tt.dot(20, random.choice(color_list))
    tt.forward(50)
    if dot_count %10 ==0:

        tt.setheading(90)
        tt.forward(50)
        tt.setheading(180)
        tt.forward(500)
        tt.setheading(0)
tt_screen.exitonclick()