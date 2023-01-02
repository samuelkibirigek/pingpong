
"""
    The ping pong game, with an interesting story behind it
    was a tremendous success. Built by a fresh Atari company
    recruit Allan Alcorn as a task to prove his programming capabilities.
"""
from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.listen()
screen.tracer(0)

l_paddle = Paddle()
r_paddle = Paddle()

l_paddle.position((-350, 0))
r_paddle.position((350, 0))

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
