import turtle 
screen=turtle.Screen()
screen.bgcolor("orange")
screen.title("Turtle spiral square")
pen=turtle.Turtle()
size=0
while True:
    for i in range(4):
        pen.forward(size+1)
        pen.left(90)
        size-=20
    size+=1
turtle.done()
