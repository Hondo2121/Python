'''
Test this.
https://tritech-testsite.smapply.io/

Get the code: 10.183.1.26 code python
Plot circle data using python
- Change the background color
- Change the graph line colors
- Change the plot line color
- Change the plot dot color
- Label the graph with text Plotting Circumference and Diameter
- Label the axis with text (Circumference and Diameter)
- Upload to github with your name initials or name attached (plot-circle-list-cwc.py

'''

import turtle
import math
wdth = 800; hgth = 800; bgstring = "#ff00ff"
red = "#cc0000"; green = "#00cc00"; blue = "#0000cc"

def grid(t):
	x = 0; y = 0
	while (x < 400):
		t.color(red)
		t.penup()
		t.goto(x,y)
		t.pendown()
		t.goto(x,y+400)
		x = x + 50
	x = 0; y = 0
	while (y < 400):
		t.color(red)
		t.penup()
		t.goto(x,y)
		t.pendown()
		t.goto(x+400,y)
		y = y + 50
	
	t.penup()

def setlabels(t):
	t.penup()
	t.goto(-175,100)
	t.pendown()
	t.color("black")
	t.write("Circumference", font=("Arial", 16, "normal"))
	t.penup()
	t.goto(100,-75)
	t.pendown()
	t.write("Diameter", font=("Arial", 16, "normal"))
	t.penup()
	t.goto(50,-200)
	t.write("Plot Graph", font=("Arial", 32, "bold"))
	t.penup()
	t.goto(-180,200)
	t.write("Circles", font=("Wingdings", 32, "bold"))

def plotCircles(t):
	d =  [3.3, 3.5, 33.0, 30.15] 
	c =  [3*12.8,  3*1.8, 3*19.7, 3* 8.7] 
	dsorted = sorted (d, key = float)
	csorted = sorted(c , key = float)
	t.goto(0,0)
	t.pendown()
	t.dot(3, green)
	t.goto(dsorted[0],csorted[0])
	t.dot(3, green)
	t.goto(dsorted[1],csorted[1])
	t.dot(3, green)
	t.goto(dsorted[2],csorted[2])
	t.dot(3, green)
	t.goto(dsorted[3],csorted[3])
	t.dot(3, green)
	
def main():
	try:
		turtle.TurtleScreen._RUNNING = True
		# get wdth and hgth globally
		turtle.screensize(canvwidth=wdth, canvheight=hgth, bg=bgstring)
		print(turtle.Screen().screensize())
		w = turtle.Screen()
		t = turtle.Turtle()
		t.speed(0)
		t.hideturtle()
		setlabels(t)
		grid(t)
		plotCircles(t)
		w.exitonclick()
	finally:
		turtle.Terminator()
	
if __name__ == '__main__':
	main()

'''
	# Using sorted + key 
	Output = sorted(Input, key = float) 
	# Using sorted + key 
	Output = sorted(Input, key = float) 
'''
