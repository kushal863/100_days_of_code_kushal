from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score=0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.write(f"score: {self.score}",align="center",font=('Arial', 20, 'normal'))


    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"score: {self.score}",align="center",font=('Arial', 20, 'normal'))

        