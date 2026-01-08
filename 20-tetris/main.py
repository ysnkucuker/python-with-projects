import turtle
import random
import time

# Constants
GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = 20
DELAY = 0.5  # seconds per drop

# Tetromino shapes
SHAPES = {
    'I': [[1,1,1,1]],
    'O': [[1,1],[1,1]],
    'T': [[0,1,0],[1,1,1]],
    'S': [[0,1,1],[1,1,0]],
    'Z': [[1,1,0],[0,1,1]],
    'J': [[1,0,0],[1,1,1]],
    'L': [[0,0,1],[1,1,1]]
}

COLORS = {
    'I': 'cyan', 'O': 'yellow', 'T': 'purple',
    'S': 'green', 'Z': 'red', 'J': 'blue', 'L': 'orange'
}


# Screen setup
screen = turtle.Screen()
screen.title("Tetris")
screen.bgcolor("black")
screen.setup(width=GRID_WIDTH*BLOCK_SIZE+100, height=GRID_HEIGHT*BLOCK_SIZE+100)
screen.tracer(0)

# Pen
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)

# Game state
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
score = 0

# Current piece
current_piece = None
current_x = 0
current_y = 0

# Draw game border
def draw_border():
    pen.color("white")
    pen.pensize(3)
    pen.penup()
    x_start = -GRID_WIDTH*BLOCK_SIZE//2
    y_start = -GRID_HEIGHT*BLOCK_SIZE//2
    pen.goto(x_start, y_start)
    pen.pendown()
    for _ in range(2):
        pen.forward(GRID_WIDTH*BLOCK_SIZE)
        pen.left(90)
        pen.forward(GRID_HEIGHT*BLOCK_SIZE)
        pen.left(90)
    pen.penup()

def draw_block(x, y, color):
    pen.goto(x*BLOCK_SIZE - GRID_WIDTH*BLOCK_SIZE//2, y*BLOCK_SIZE - GRID_HEIGHT*BLOCK_SIZE//2)
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(BLOCK_SIZE)
        pen.left(90)
    pen.end_fill()

def draw_grid():
    pen.clear()
    draw_border()  # <-- border çiz
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y][x]:
                draw_block(x, y, grid[y][x])
    if current_piece:
        shape, color = current_piece
        for dy, row in enumerate(shape):
            for dx, cell in enumerate(row):
                if cell:
                    draw_block(current_x+dx, current_y+dy, color)
    pen.goto(-50, GRID_HEIGHT*BLOCK_SIZE//2 + 20)
    pen.color("white")
    pen.write(f"Score: {score}", font=("Arial", 16, "bold"))

def valid_move(shape, x, y):
    for dy, row in enumerate(shape):
        for dx, cell in enumerate(row):
            if cell:
                gx = x + dx
                gy = y + dy
                if gx < 0 or gx >= GRID_WIDTH or gy < 0 or gy >= GRID_HEIGHT:
                    return False
                if grid[gy][gx]:
                    return False
    return True

def place_piece():
    global current_piece, current_x, current_y, score
    shape, color = current_piece
    for dy, row in enumerate(shape):
        for dx, cell in enumerate(row):
            if cell:
                grid[current_y+dy][current_x+dx] = color
    clear_lines()
    new_piece()

def clear_lines():
    global grid, score
    new_grid = []
    cleared = 0
    for row in grid:
        if all(row):
            cleared += 1
        else:
            new_grid.append(row)
    for _ in range(cleared):
        new_grid.insert(0, [0]*GRID_WIDTH)
    grid[:] = new_grid
    score += cleared * 100

def new_piece():
    global current_piece, current_x, current_y
    shape_name = random.choice(list(SHAPES.keys()))
    current_piece = [SHAPES[shape_name], COLORS[shape_name]]
    current_x = GRID_WIDTH//2 - len(current_piece[0][0])//2
    current_y = GRID_HEIGHT - len(current_piece[0])
    if not valid_move(current_piece[0], current_x, current_y):
        game_over()

def move_left():
    global current_x
    if current_piece and valid_move(current_piece[0], current_x-1, current_y):
        current_x -= 1

def move_right():
    global current_x
    if current_piece and valid_move(current_piece[0], current_x+1, current_y):
        current_x += 1

def move_down():
    global current_y
    if current_piece and valid_move(current_piece[0], current_x, current_y-1):
        current_y -= 1
    else:
        place_piece()

def rotate():
    global current_piece
    if current_piece:
        shape, color = current_piece
        new_shape = list(zip(*shape[::-1]))
        if valid_move(new_shape, current_x, current_y):
            current_piece[0] = [list(row) for row in new_shape]

def game_over():
    pen.goto(-100,0)
    pen.color("red")
    pen.write("GAME OVER", font=("Arial", 24, "bold"))
    screen.update()
    time.sleep(3)
    screen.bye()

# Keyboard
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_down, "Down")
screen.onkeypress(rotate, "Up")

# Start first piece
new_piece()
draw_grid()

# Main loop
while True:
    screen.update()
    move_down()
    draw_grid()
    time.sleep(DELAY)
