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

states = df['state'].to_list()
answers = []
while len(answers) <50:
    answer_state = screen.textinput(title =f"{scores}/50 States Correct", prompt="What's another state's name").title()
    # print(df.loc[df['state']=='Alaska']['x'].values[0])
    answers.append(answer_state)

    if answer_state =="Exit":
         break

    try:
        if answer_state in states:
            state_data = df[df['state']==str(answer_state)]
            my_turtle.goto(int(state_data.x),int(state_data.y))
            my_turtle.write(state_data.state.item())
        else:
             pass

    except Exception as e:
            print(f"Enter Corrent State Name : {e}")
            

    scores+=1

df[~df['state'].isin(answers)].to_csv('Not_answered.csv',index=False)

screen.exitonclick()