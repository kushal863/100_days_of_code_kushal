from turtle import Turtle

ALGNMENT="center"
FONT =('Courier', 20, 'normal')



class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score=0
        with open('data.txt') as highest_score:
            self.high_score = int(highest_score.read())
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        # if self.score >self.high_score:
        #     self.high_score = self.score        
        self.write(f"score: {self.score} high score : {self.high_score}",align=ALGNMENT,font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt','w') as data:
                data.write(f"{self.high_score}")
            
        self.score=0
        self.update_scoreboard()



    def increase_score(self):
        self.score+=1
        self.update_scoreboard()
        

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align=ALGNMENT,font=FONT)

        