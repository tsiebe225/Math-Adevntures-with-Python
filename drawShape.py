import turtle

def drawShape(turtleImp , length = 100,sides = 4):
    for i in range(0,sides):
        turtleImp.right(360/sides)
        turtleImp.forward(length)
        i=i+1

def drawShapeRot(turtleImp, numberofRepreats = 20, angleDelta = 18, length = 100, sides = 4):
    for i in range(0,numberofRepreats):
        drawShape(turtleImp,length,sides)
        turtleImp.right(angleDelta)

def drawShapeSpiralOut(turtleImp, numberofRepreats = 20, angleDelta = 18, length = 100, sides = 4, posDelta = 25):
    for i in range(0,numberofRepreats):
        drawShape(turtleImp,length,sides)
        turtleImp.right(angleDelta)
        turtleImp.forward(posDelta)

wn = turtle.Screen()

keith = turtle.Turtle()

drawShapeSpiralOut(keith)

wn.exitonclick()