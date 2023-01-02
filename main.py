
"""
    The ping pong game, with an interesting story behind it
    was a tremendous success. Built by a fresh Atari company
    recruit Allan Alcorn as a task to prove his programming capabilities.
"""
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.listen()
screen.tracer(0)

l_paddle = Paddle()
r_paddle = Paddle()
ball = Ball()
score = Score()

l_paddle.position((-350, 0))
r_paddle.position((350, 0))

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.the_speed)
    screen.update()
    ball.move()
    score.scoreboard()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 370:
        if score.l_score == 10:
            score.game_over()
        score.update_l_score()
        ball.reset_position()
        ball.bounce_x()
    if ball.xcor() < -370:
        score.game_over()
        score.update_r_score()
        ball.reset_position()
        ball.bounce_x()


screen.exitonclick()
