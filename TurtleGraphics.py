import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
        
def drawPolygon (myTurtle, sides):
    for s in range (sides):
        myTurtle.forward(50)
        myTurtle.right(360/sides)
        
def fillCorner (myTurtle, corner):
    drawSquare (myTurtle, 100)
    if corner==1:
        myTurtle.begin_fill()
        drawSquare (myTurtle, 50)
        myTurtle.end_fill()
    elif corner==2:
        myTurtle.forward(50)
        myTurtle.begin_fill()
        drawSquare (myTurtle, 50)
        myTurtle.end_fill()
    elif corner==3:
        myTurtle.right(90)
        myTurtle.forward(50)
        myTurtle.left(90)
        myTurtle.begin_fill()
        drawSquare (myTurtle, 50)
        myTurtle.end_fill()
    else :
        myTurtle.right(90)
        myTurtle.forward(100)
        myTurtle.left(90)
        myTurtle.forward(50)
        myTurtle.left(90)
        myTurtle.forward(50)
        myTurtle.right(90)
        myTurtle.begin_fill()
        drawSquare (myTurtle, 50)
        myTurtle.end_fill()
        
def squaresInSquares(myTurtle,num):
    size=200
    drawSquare(myTurtle, size)
    myTurtle.up()
    myTurtle.right(45)
    myTurtle.forward(15)
    myTurtle.left(45)
    myTurtle.down()
    for n in range (num-1):
        size=size/1.15
        drawSquare(myTurtle,size)
        myTurtle.up()
        myTurtle.right(45)
        myTurtle.forward(15)
        myTurtle.left(45)
        myTurtle.down()
    
def main():
    myTurtle = turtle.Turtle()
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
