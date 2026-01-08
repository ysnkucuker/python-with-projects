import turtle
import random

# Game Screen
screen = turtle.Screen()
screen.title("Turtle Yakalama Oyunu")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# Variables
score = 0
time_left = 20

# Score text
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-250, 260)

# Time text
time_writer = turtle.Turtle()
time_writer.hideturtle()
time_writer.penup()
time_writer.goto(150, 260)

# Player
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)

# Score
def update_score():
    score_writer.clear()
    score_writer.write(f"Score: {score}", font=("Arial", 14, "bold"))

# Timer
def update_time():
    time_writer.clear()
    time_writer.write(f"Time: {time_left}", font=("Arial", 14, "bold"))

# Turtle location
def move_turtle():
    if time_left > 0:
        x = random.randint(-250, 250)
        y = random.randint(-200, 200)
        player.goto(x, y)
        screen.ontimer(move_turtle, 700)  # 0.7 saniye sonra tekrar

# Click
def turtle_clicked(x, y):
    global score
    if time_left > 0:
        score += 10
        update_score()

# Countdown
def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        update_time()
        screen.ontimer(countdown, 1000)
    else:
        game_over()


def game_over():
    player.hideturtle()
    score_writer.goto(0, 0)
    score_writer.write("GAME OVER", align="center", font=("Arial", 24, "bold"))

# Click Listener
player.onclick(turtle_clicked)

# Start
update_score()
update_time()
move_turtle()
countdown()

screen.mainloop()
