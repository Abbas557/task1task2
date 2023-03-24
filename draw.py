import turtle
t = turtle.Turtle()
t.speed(5) 
t.forward(100)
# Move the turtle to the starting point
t.penup()
t.goto(-100, 0)
t.pendown()

# Draw the house shape
t.forward(200)
t.left(90)
t.forward(150)
t.left(90)
t.forward(200)
t.left(90)
t.forward(150)
t.left(45)
t.forward(100)
t.left(90)
t.forward(100)
t.left(45)
t.forward(150)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)

# Hide the turtle
t.hideturtle()

# Keep the window open until it's closed manually
turtle.done()
