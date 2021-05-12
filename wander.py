import turtle
from random import randint

def wander(turtleHolder):
    while True:
        turtleHolder.forward(3)
        if turtleHolder.xcor() >= 200 or turtleHolder.xcor()<-200 or turtleHolder.ycor() <=-200 or turtleHolder.ycor()>200:
            turtleHolder.lt(randint(90,180))

wn = turtle.Screen()

keith = turtle.Turtle()
keith.speed(0)
wander(keith)


wn.exitonclick()