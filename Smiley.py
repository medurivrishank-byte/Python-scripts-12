import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()
t.speed(3)
t.penup()

# Draw the face (yellow circle)
t.goto(0, -100)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()
t.penup()

# Draw the eyes (black dots)
t.goto(-35, 30)
t.pendown()
t.dot(25, "black")
t.penup()

t.goto(35, 30)
t.pendown()
t.dot(25, "black")
t.penup()

# Draw the smile
t.goto(-60, -20)
t.pendown()
t.pencolor("black")
t.pensize(10)
t.setheading(-60)
t.circle(70, 120) # Draw an arc for the smile

# Hide the turtle cursor and keep the window open
t.hideturtle()
turtle.done()