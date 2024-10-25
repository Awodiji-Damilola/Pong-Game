from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Initialize screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)

# Get target score from the user
target_score = int(screen.textinput("Pong Game", "Enter the target score (e.g., 10, 20, etc.): "))

# Initialize paddles, ball, and scoreboard
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Variables to track key presses for continuous movement
r_up_pressed = False
r_down_pressed = False
l_up_pressed = False
l_down_pressed = False

# Paddle movement functions
def move_r_paddle():
    if r_up_pressed:
        r_paddle.go_up()
    if r_down_pressed:
        r_paddle.go_down()

def move_l_paddle():
    if l_up_pressed:
        l_paddle.go_up()
    if l_down_pressed:
        l_paddle.go_down()

# Key press and release handlers
def r_paddle_up_press():
    global r_up_pressed
    r_up_pressed = True

def r_paddle_down_press():
    global r_down_pressed
    r_down_pressed = True

def l_paddle_up_press():
    global l_up_pressed
    l_up_pressed = True

def l_paddle_down_press():
    global l_down_pressed
    l_down_pressed = True

def r_paddle_up_release():
    global r_up_pressed
    r_up_pressed = False

def r_paddle_down_release():
    global r_down_pressed
    r_down_pressed = False

def l_paddle_up_release():
    global l_up_pressed
    l_up_pressed = False

def l_paddle_down_release():
    global l_down_pressed
    l_down_pressed = False

# Listen for key events
screen.listen()
screen.onkeypress(r_paddle_up_press, 'Up')
screen.onkeyrelease(r_paddle_up_release, 'Up')
screen.onkeypress(r_paddle_down_press, 'Down')
screen.onkeyrelease(r_paddle_down_release, 'Down')

screen.onkeypress(l_paddle_up_press, 'w')
screen.onkeyrelease(l_paddle_up_release, 'w')
screen.onkeypress(l_paddle_down_press, 's')
screen.onkeyrelease(l_paddle_down_release, 's')

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    move_r_paddle()
    move_l_paddle()

    # Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect when r_paddle misses
    if ball.xcor() > 400:
        time.sleep(1)
        ball.reset_position()
        scoreboard.l_point()

    # Detect when l_paddle misses
    if ball.xcor() < -400:
        time.sleep(1)
        ball.reset_position()
        scoreboard.r_point()

    # End game when the target score is reached
    if scoreboard.l_score == target_score:
        game_is_on = False
        scoreboard.game_over("Left Player")
    elif scoreboard.r_score == target_score:
        game_is_on = False
        scoreboard.game_over("Right Player")

screen.exitonclick()
