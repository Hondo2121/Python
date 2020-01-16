import turtle
import math
import random
#global variable(s)
#define global variables here
#example:  xM = 0 

def mike(t):
	#change global variables
    # example :  global xM = 200    
    t.forward(100)

def main():
    try:
        turtle.TurtleScreen._RUNNING = True
        turtle.screensize(canvwidth=700, canvheight=700, bg=None)
        print(turtle.Screen().screensize())
        w = turtle.Screen()
        t = turtle.Turtle()
        mike(t)
        w.exitonclick()
    finally:
        turtle.Terminator()
	
if __name__ == '__main__':
    main()

