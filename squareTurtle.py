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

def drawShape(turtleImp , length = 100,sides = 4):
    for i in range(0,sides):
        turtleImp.right(360/sides)
        turtleImp.forward(length)
        i=i+1

def drawShapeRot(turtleImp, numberofRepreats = 20, angleDelta = 18, length = 100, sides = 4):
    for i in range(0,numberofRepreats):
        drawShape(turtleImp,length,sides)
        turtleImp.right(angleDelta)

def increasingSizeShapeRotate(turtleImp, numberofRepreats = 20, angleDelta = 18, length = 100,lengthDelta = 20, sides = 4):
    for i in range(0,numberofRepreats):
        drawShape(turtleImp,length,sides)
        length = length + lengthDelta
        turtleImp.right(angleDelta)

def drawShapeSpiralOffsetIncreasing(turtleImp, numberofRepreats = 20, angleDelta = 18, length = 100, lengthDelta = 20, sides = 4, posDelta = 25):
    for i in range(0,numberofRepreats):
        drawShape(turtleImp,length,sides)
        length = length + lengthDelta
        turtleImp.right(angleDelta)
        turtleImp.forward(posDelta)

def star(turtleHolder, length = 100):
    for i in range(0,5):
        turtleHolder.forward(length)
        turtleHolder.right(144)

def starSpiral(turtleHolder, length = 100,lengthDelta = 5, repeats = 20, angleDelta = 18):
    for i in range(0,repeats):
        star(turtleHolder,length)
        length = length + lengthDelta
        turtleHolder.right(angleDelta)

def starSpiralIncrease(turtleHolder, length = 100,lengthDelta = 5, repeats = 20, angleDelta = 18, angleDeltaIncrease = 5):
    for i in range(0,repeats):
        star(turtleHolder,length)
        length = length + lengthDelta
        turtleHolder.right(angleDelta)
        angleDelta = angleDelta + angleDeltaIncrease

wn = turtle.Screen()

keith = turtle.Turtle()

starSpiral(keith,150,5,60,3)

wn.exitonclick()