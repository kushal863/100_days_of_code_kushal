from turtle import Turtle

STARTING_POSSITIONS=[(0,0),(-20,0),(-40,0)]
class Snake:

    def __init__(self) -> None:
        self.segments =[]
        self.create_snake()
        

    def create_snake(self):
        for possition in STARTING_POSSITIONS:

            segment =Turtle(shape='square')
            segment.penup()
            segment.color('White')
            segment.goto(possition)
            self.segments.append(segment)
    def move(self):
        

        for seg in range(2,0,-1):
            x_new = self.segments[seg-1].xcor()
            y_new = self.segments[seg-1].ycor()

            self.segments[seg].goto(x_new,y_new)
        self.segments[0].forward(20)