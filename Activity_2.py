import turtle
turtle.Screen().bgcolor("orange")
pen=turtle.Turtle()
for i in range(3):
    pen.forward(100)
    pen.left(120)
pen.penup()
pen.left(90)
pen.forward(50)
pen.pendown()
pen.right(90)
for i in range(3):
    pen.forward(100)
    pen.right(120)
turtle.done()