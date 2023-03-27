from turtle import Turtle

STARTING_POSSITIONS=[(0,0),(-20,0),(-40,0)]
MOVING_DISTANCE =20
UP =90
DOWN=270
LEFT =180
RIGHT =0
class Snake:

    def __init__(self) -> None:
        self.segments =[]
        self.create_snake()
        self.head =self.segments[0]
        

    def create_snake(self):
        for possition in STARTING_POSSITIONS:
            self.add_segment(possition=possition)



    def add_segment(self,possition):
            segment =Turtle(shape='square')
            segment.penup()
            segment.color('White')
            segment.goto(possition)
            self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())


        
    def move(self):
        

        for seg in range(2,0,-1):
            x_new = self.segments[seg-1].xcor()
            y_new = self.segments[seg-1].ycor()

            self.segments[seg].goto(x_new,y_new)
        self.head.forward(MOVING_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)

        
    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)

