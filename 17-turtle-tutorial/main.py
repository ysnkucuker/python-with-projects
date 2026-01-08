import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")


#turtle_instance = turtle.Turtle()
#turtle_instance.forward(100)

#turtle_instance2 = turtle.Turtle()
#turtle_instance2.left(45)
#turtle_instance2.forward(100)

turtle_square = turtle.Turtle()
# turtle_square.forward(100)
# turtle_square.left(90)
# turtle_square.forward(100)
# turtle_square.left(90)
# turtle_square.forward(100)
# turtle_square.left(90)
# turtle_square.forward(100)

for i in range(4):
    turtle_square.left(90)
    turtle_square.forward(100)

turtle.done()