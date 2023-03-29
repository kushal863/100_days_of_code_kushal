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
        for possition_n in STARTING_POSSITIONS:
            self.add_segment(possition=possition_n)



    def add_segment(self,possition):
            segment =Turtle(shape='square')
            
            segment.color('white')
            segment.penup()
            segment.goto(possition)
            self.segments.append(segment)


    def extend(self):
        print(self.segments)
        self.add_segment(self.segments[-1].position())
        
    def reset(self):
        for seg in self.segments:
            seg.goto(900,900)
        self.segments.clear()
        self.create_snake()
        self.head =self.segments[0]

 


        
    def move(self):
        

        for seg in range(len(self.segments)-1,0,-1):
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

