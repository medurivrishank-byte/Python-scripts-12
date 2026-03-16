import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(300,400)
pen=turtle.Turtle()
sides=int(input("Enter the number of sides of your shape: "))
angle=360/sides
length=100
for i in range(sides):
    pen.forward(length)
    pen.right(angle)
turtle.done()