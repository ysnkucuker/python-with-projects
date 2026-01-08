import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("Spiral Helix")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")
turtle.speed("fastest")

turtle_colors = ["red","purple","blue","orange","yellow","white"]

for i in range(15):
    turtle_instance.color(turtle_colors[i % 6])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)


turtle.done()