import turtle
import time
import random

# Screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Borders (STRICT)
TOP = 220
BOTTOM = -280
LEFT = -280
RIGHT = 280

# Game state
score = 0
paused = False
game_over_state = False
start_time = time.time()

# Load top 3 scores
def load_scores():
    try:
        with open("scores.txt", "r") as f:
            return sorted([int(line) for line in f], reverse=True)[:3]
    except:
        return []

def save_score(new_score):
    scores = load_scores()
    scores.append(new_score)
    scores = sorted(scores, reverse=True)[:3]
    with open("scores.txt", "w") as f:
        for s in scores:
            f.write(str(s) + "\n")
    return scores

high_scores = load_scores()

# Scoreboard
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.color("white")
score_writer.goto(0, 255)

def update_scoreboard():
    elapsed = int(time.time() - start_time)
    highs = " - ".join(str(s) for s in high_scores) if high_scores else "None"
    score_writer.clear()
    score_writer.write(
        f"Score: {score} | Time: {elapsed}s | High Scores: {highs}",
        align="center",
        font=("Courier", 13, "bold")
    )

update_scoreboard()

# Bottom info
info_writer = turtle.Turtle()
info_writer.hideturtle()
info_writer.penup()
info_writer.color("gray")
info_writer.goto(0, -250)
info_writer.write("Press P to Pause / Resume", align="center",
                  font=("Courier", 12, "normal"))

# Game Over text
game_over_writer = turtle.Turtle()
game_over_writer.hideturtle()
game_over_writer.penup()
game_over_writer.color("red")
game_over_writer.goto(0, -200)

# Draw walls
wall = turtle.Turtle()
wall.hideturtle()
wall.color("white")
wall.pensize(3)
wall.penup()
wall.goto(LEFT, TOP)
wall.pendown()
wall.goto(RIGHT, TOP)
wall.goto(RIGHT, BOTTOM)
wall.goto(LEFT, BOTTOM)
wall.goto(LEFT, TOP)

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()

def place_food():
    x = random.randint(LEFT + 20, RIGHT - 20)
    y = random.randint(BOTTOM + 20, TOP - 20)
    food.goto(x, y)

place_food()

segments = []

# Movement
def go_up():
    if head.direction != "down" and not paused:
        head.direction = "up"

def go_down():
    if head.direction != "up" and not paused:
        head.direction = "down"

def go_left():
    if head.direction != "right" and not paused:
        head.direction = "left"

def go_right():
    if head.direction != "left" and not paused:
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

# Pause
def toggle_pause():
    global paused
    paused = not paused

# Keyboard
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")
screen.onkeypress(toggle_pause, "p")

# Game over
def game_over():
    global game_over_state, high_scores
    game_over_state = True
    high_scores = save_score(score)
    update_scoreboard()
    game_over_writer.write(
        "GAME OVER\nPress R to Restart",
        align="center",
        font=("Courier", 16, "bold")
    )

# Restart
def restart():
    global score, game_over_state, start_time
    score = 0
    game_over_state = False
    start_time = time.time()

    head.goto(0, 0)
    head.direction = "stop"

    for s in segments:
        s.goto(1000, 1000)
    segments.clear()

    game_over_writer.clear()
    place_food()
    update_scoreboard()

screen.onkeypress(restart, "r")

# Main loop
while True:
    screen.update()

    if paused or game_over_state:
        time.sleep(0.1)
        continue

    update_scoreboard()

    # Wall collision (STRICT)
    if (head.xcor() >= RIGHT or head.xcor() <= LEFT or
        head.ycor() >= TOP or head.ycor() <= BOTTOM):
        game_over()
        continue

    # Food collision
    if head.distance(food) < 20:
        place_food()

        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()
        segments.append(new_segment)

        score += 10

    # Move body
    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i - 1].xcor(), segments[i - 1].ycor())

    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Self collision
    for s in segments:
        if s.distance(head) < 20:
            game_over()

    time.sleep(0.1)
