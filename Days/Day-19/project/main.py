from turtle import Turtle, Screen
import random

# t = Turtle(shape='turtle')

t_screen = Screen()

t_screen.setup(width=500,height=400)

user_bet = t_screen.textinput(title="Make you bet",prompt="Which turtle will win the race? enter a color: " )

y_possitions = [-100,-60,-20,20,60,100]
color = ["red","orange","yellow","green","blue","purple"]

turtle_instances =[]
for turtle_index in range(0,6):
    new_turtle =Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=-220,y=y_possitions[turtle_index])
    new_turtle.color(color[turtle_index])
    turtle_instances.append(new_turtle)

is_race_on=True
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_instances:
        
        if turtle.xcor()> 250:
            is_race_on=False
            winning_color = turtle.pencolor()
            if winning_color ==user_bet:
                print(f"You're won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        ran_num = random.randint(1,10)
        

        turtle.forward(ran_num)

    








t_screen.exitonclick()