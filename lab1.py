import turtle

'''
Commands that Casey the Turtle understands:
- pendown()
    put turtle's pen down
- penup()
    pick up turtle's pen
- forward(x)
    move forward by x distance
- right(x)
    turn turtle right by x degrees
- left(x)
    turn turtle left by x degrees
'''

casey = turtle.Turtle()
casey.shape("turtle")

# Draw parallelogram.
casey.pendown()
casey.forward(250)
casey.left(90)
casey.forward(70)
casey.left(90)
casey.forward(250)
casey.left(90)
casey.forward(70)

# Move turtle 50 spaces below without drawing anything.
casey.penup()
casey.left(180)
casey.forward(150)

# Draw square (aka a lame parallelogram).
casey.pendown()
casey.forward(70)
casey.right(90)
casey.forward(70)
casey.right(90)
casey.forward(70)
casey.right(90)
casey.forward(70)

# Move turtle out of the way so it doesn't block my beautiful drawing.
casey.penup()
casey.forward(50)

turtle.mainloop()
