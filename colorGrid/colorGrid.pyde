def setup():
    size(600,600)
    colorMode(HSB)

def draw():
    background(0)
    translate(20,20)
    for x in range(30):
        for y in range(30):
            d = dist(30*x,30*y,mouseX,mouseY)
            fill(.5*d,255,255)
            rect(30*x,30*y,25,25)
