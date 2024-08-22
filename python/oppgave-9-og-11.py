import turtle
turtle

def rectangle(turtle, x, y, height, width, color):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    turtle.goto(x+width, y)
    turtle.goto(x+width, y+height)
    turtle.goto(x, y+height)
    turtle.goto(x, y)
    turtle.up()
    turtle.end_fill()

def triangle(turtle, x, y, height, width, color):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    turtle.goto(x+width, y)
    turtle.goto(x+width/2, y+height)
    turtle.goto(x, y)
    turtle.end_fill()
    turtle.up()

# Pipe
rectangle(turtle, -40, 90, 35, 15, "black")

# Hovedfasaden
rectangle(turtle, -50, 0, 75, 125, "blue")

# Tak
triangle(turtle, -75, 75, 50, 175, "blue")

# Dør
rectangle(turtle, -30, 0, 50, 30, "cyan")

# Vindu
rectangle(turtle, 25, 15, 30, 30, "yellow")

# Gjemmer skilpadden
turtle.goto(1000, 1000)

# Hindrer vinduet i å lukke
turtle.mainloop()