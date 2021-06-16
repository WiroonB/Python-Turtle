import turtle

def draw_pentagon(turtle, x, y):
	turtle.penup()
	turtle.goto((x,y))
	turtle.pendown()

	turtle.begin_fill()
	turtle.setheading(0)
	turtle.forward(50)
	turtle.left(72)
	turtle.forward(50)
	turtle.left(72)
	turtle.forward(50)
	turtle.left(72)
	turtle.forward(50)
	turtle.left(72)
	turtle.forward(50)
	turtle.end_fill()

pentagon = turtle.Turtle()

pentagon.speed(5)

pentagon.color("red", "yellow")

draw_pentagon(pentagon,-250,100)
draw_pentagon(pentagon,-100,100)
draw_pentagon(pentagon,50,100)
draw_pentagon(pentagon,200,100)
draw_pentagon(pentagon,-250,-50)
draw_pentagon(pentagon,-100,-50)
draw_pentagon(pentagon,50,-50)
draw_pentagon(pentagon,200,-50)


turtle.done()

	