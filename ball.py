from turtle import Turtle
import random

#X_RANDOM = random.randint(0, 300)
#Y_RANDOM = random.randint(0, 300)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.speed("slowest")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()

    #this will make the ball move up and also to the right
    def move_ball(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(x=new_x, y=new_y)