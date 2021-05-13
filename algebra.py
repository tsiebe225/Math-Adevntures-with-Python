from math import sqrt

def equation(a,b,c,d):
    return(d-b)/(a-c)

def quad(a,b,c):

    ans1 = (-b+sqrt((b*b)-4*a*c))/(2*a)
    ans2 = (-b - sqrt((b * b) - 4 * a * c)) / (2 * a)
    ansList = [ans1,ans2]
    return ansList

def g(x):
    return 6*x**3+31*x**2+3*x-10

def plug():
    x = -100
    while x<100:
        if g(x) == 0:
            print("x =",x)
            break
        else:
            x+=.25

print(quad(2,7,-15))
plug()
