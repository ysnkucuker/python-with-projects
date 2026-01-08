import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light green")
drawing_board.title("Inner Square")

turtle_square = turtle.Turtle()

turtle_square.color("blue")


def shrinking_square(size):
    while(size > 0):
        for i in range(4):
            turtle_square.forward(size)
            turtle_square.right(90)
        size = size - 10

shrinking_square(150)

turtle.done()