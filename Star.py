import turtle

def draw_star(t, size, color):
	angle = 144
	t.width(3)
	l = ["#ffffff", "#f0f000", "#00ff00", "#0000ff", "#000000"]
	t.fillcolor(color)
	t.begin_fill()
	for side in range(5):
		t.speed(5)
		t.pencolor(l[side])
		t.forward(size)
		t.right(angle)
		t.forward(size)
		t.right(72 - angle)
	t.end_fill()
	return
		
def main():
	x = 0; y = 0
	t = turtle.Turtle()
	w = turtle.Screen()
	w.setup(1000, 700)
	w.clear()
	w.bgcolor("pink")
	t.setposition(50,50)
	draw_star(t, 100, "red")

	w.exitonclick()

def stars(t,size,color, num):
		for i in range(num+1):
			if(i ==0):
				i+=1
			if(i < 4 and i >0):
				t.setposition(0, (200-(i*100)))
				draw_star(t, 25, "red")
			if(i > 3 and i < 6):
				t.setposition(-100, (100-((i-3)*100)))
				draw_star(t, 25, "red")
			if(i >= 6 and i < 8):
				t.setposition(100,(200-((i-5)*100)))
				draw_star(t, 25, "red")
		else:
			print("Done!")
	

if __name__ == '__main__':
	main()

'''''''''''''''''
	t.penup()
	t.setposition(100,-100)
	draw_star(t, 50, "red")
	t.penup()
	t.setposition(-100,-100)
	draw_star(t, 50, "red")
	t.penup()
	t.setposition(-100,100)
	draw_star(t, 50, "red")
'''''''''''''''''
