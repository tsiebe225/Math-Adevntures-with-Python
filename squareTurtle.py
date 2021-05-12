import turtle

def square(turtleImp , length):
    for i in range(0,4):
        turtleImp.right(90)
        turtleImp.forward(length)
        i=i+1

def rotateSquare(turtleImp, numberofSquares,degreesofRot,length):
    for i in range(0,numberofSquares):
        square(turtleImp,length)
        turtleImp.right(degreesofRot)

def triangle(turtleHolder, length = 100):
    for i in range(0,3):
        turtleHolder.right(120)
        turtleHolder.forward(length)

wn = turtle.Screen()

keith = turtle.Turtle()

triangle(keith, 200)

wn.exitonclick()