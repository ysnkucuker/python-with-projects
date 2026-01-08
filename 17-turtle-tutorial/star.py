import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")


turtle_star = turtle.Turtle()

# for i in range(10):
#     turtle_star.forward(100)
#     turtle_star.left(135)
#     turtle_star.forward(100)
#     turtle_star.left(135)

for i in range(5):
    turtle_star.right(144)
    turtle_star.forward(100)

turtle.done()