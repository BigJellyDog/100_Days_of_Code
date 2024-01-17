"""Pong the game made by Jelly"""
import time
from turtle import Screen, Turtle
from paddles import Paddle
from ball import Ball
from screboard import Scoreboard
# Set up Screen

screen = Screen()
screen.bgcolor("black")
screen.screensize(800, 600)
screen.title("Pong by Jelly")
screen.tracer(0)

# Set up the paddles and make them move
player1 = Paddle((350, 0))
player2 = Paddle((-350, 0))
# Set up the ball
ball = Ball()
scoreboard = Scoreboard()
screen.listen()


screen.onkeypress(player1.up, "Up")
screen.onkeypress(player1.down, "Down")
screen.onkeypress(player2.up, "w")
screen.onkeypress(player2.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.moving_ball()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if (
        ball.distance(player1) < 50 and ball.xcor() > 320
        or ball.distance(player2) < 50 and ball.xcor() > -320
    ):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# Detect collision with the borders

# Detect collision with the players

# Counting the points and make a line in the middle


screen.exitonclick()
