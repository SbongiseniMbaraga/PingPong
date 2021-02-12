from turtle import Screen
from paddles import Paddles
from ball import Ball
from scoreboard import Scoreboard
import time

#set screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

#adds the shape on to the appropriate position
POSITIONS = (350, -350, 0)
r_paddles = Paddles()
r_paddles.set_shape_of_paddles()
r_paddles.set_position(POSITIONS[0], POSITIONS[2])
#left paddle
l_paddles = Paddles()
l_paddles.set_shape_of_paddles()
l_paddles.set_position(POSITIONS[1], POSITIONS[2])

#gives the user the ability to move the shape
screen.listen()
screen.onkey(r_paddles.move_shape_up, "Up")
screen.onkey(r_paddles.move_shape_down, "Down")
#left paddle
screen.onkey(l_paddles.move_shape_up, "w")
screen.onkey(l_paddles.move_shape_down, "s")

#ball object
ball = Ball()
#scoreboard object
scoreboard = Scoreboard()

#this updates the screen because I turned of the screen animation by using tracer
game_is_on = True
bounce = False

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    #detect walls and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #detect collision with r_paddle
    if ball.distance(r_paddles) < 50 and ball.xcor() > 320 or ball.distance(l_paddles) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect r player
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    #detect l player
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()