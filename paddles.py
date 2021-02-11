from turtle import Turtle
WIDTH_PADDLES = 20
HEIGHT_PADDLES = 100

class Paddles(Turtle):

    def __init__(self):
        super().__init__()

    def set_shape_of_paddles(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def set_position(self, x_pos, y_pos):
        self.goto(x=x_pos, y=y_pos)

    def move_shape_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_shape_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)