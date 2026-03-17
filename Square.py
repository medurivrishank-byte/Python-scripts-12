import turtle
turtle.Screen().bgcolor("yellow")
len=int(input("Enter the length of your square: "))
for i in range(4):
    turtle.forward(len)
    turtle.right(90)
turtle.done