from turtle import *

class TurtleBall:

    def __init__(self,color):
        __init(self,color,45,-100,-100,100,100)

    def __init__(self,color,angle,x1,y1,x2,y2):
        self.turtle = Turtle()
        self.turtle.color(color)
        self.turtle.shape("circle")
        self.turtle.left(angle)
        self.turtle.speed(0)
        self.xMin,self.yMin,self.xMax,self.yMax = x1,y1,x2,y2

    def move(self,d):
        for i in range(d):
            x,y = self.turtle.pos()
            angle = self.turtle.heading()
            if (x > self.xMax-4 or x < self.xMin+4)\
               and (y > self.yMax-4 or y < self.yMin+4):
                self.turtle.left(180)
            elif x > self.xMax-4 or x < self.xMin+4:
                self.turtle.left(180-2*angle)
            elif y > self.yMax-4 or y < self.yMin+4:
                self.turtle.left(360-2*(angle))
            self.turtle.forward(5)

    def getTurtle(self):
        return self.turtle

    def setTurtle(self, value):
        self.turtle = value
#Test program for turtles as billard balls
import turtle
from random import *

def setUpTable(xMin,yMin,side):
    draw = turtle.Turtle()
    draw.up()
    draw.goto(xMin,yMin)
    draw.down()
    for i in range(4):
        draw.forward(side)
        draw.left(90)
    draw.hideturtle()
    

def main():
    setUpTable(-200,-200,400)
    b1 = TurtleBall("blue",random()*360,-200,-200,200,200)
    b1.move(400)
    
    turtle.Screen().exitonclick()
    
main()