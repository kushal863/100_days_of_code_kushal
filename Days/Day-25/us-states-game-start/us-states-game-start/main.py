import turtle
import pandas as pd


screen = turtle.Screen()

screen.title("U.S States Games")


image = "blank_states_img.gif"

screen.addshape(image)
screen.bgpic(image)


my_turtle = turtle.Turtle()

my_turtle.hideturtle()
my_turtle.penup()
# my_turtle.shape(image)


df=pd.read_csv('50_states.csv')


scores =0
correct_states =True
for i in range(50):

    answer_state = screen.textinput(title =f"{scores}/50 States Correct", prompt="What's another state's name").title()
    # print(df.loc[df['state']=='Alaska']['x'].values[0])

    try:
        x_cor =df.loc[df['state']==str(answer_state)]['x'].values[0]
        y_cor =df.loc[df['state']==str(answer_state)]['y'].values[0]
        my_turtle.goto(x_cor,y_cor)
        my_turtle.write(answer_state)
        correct_states=True

    except Exception as e:
            print(f"Enter Corrent State Name : {e}")
            correct_states=False

    if correct_states== True:
        scores+=1
    else:
        pass
