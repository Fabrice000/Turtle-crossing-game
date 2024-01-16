from turtle import Turtle
STARTING_POSITION = (0,-200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()
    
    def go_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x,self.ycor())
    def go_left(self):
        new_x = self.xcor() - MOVE_DISTANCE      
        self.goto(new_x,self.ycor())
    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(),new_y)
    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
          
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
    def go_to_start(self):
        self.goto(STARTING_POSITION)