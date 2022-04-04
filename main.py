from scoreboard import ScoreCard
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
new_x = 0
new_y = 0

screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

game_is_on = True
left_player = 0
right_player = 0
scoreboard = ScoreCard(left_player, right_player)

a = 0.1

while game_is_on:
    ball.move()
    time.sleep(a)
    screen.update()

    # detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        if a == 0.1:
            a = 0.1
        else:
            a *= 0.9

    # detect left paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        if a == 0.1:
            a = 0.1
        else:
            a *= 0.9

    # if ball dint hit the paddle
    if ball.xcor() > 390:
        a = 0.1
        left_player += 1
        ball.reset_position()
        scoreboard.update(left_player, right_player)

    if ball.xcor() < -390:
        a = 0.1
        right_player += 1
        ball.reset_position()
        scoreboard.update(left_player, right_player)

screen.exitonclick()
