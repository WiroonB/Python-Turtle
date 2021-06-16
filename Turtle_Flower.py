import turtle

flower = turtle.Turtle()

flower.color("red", "yellow")

flower.speed(10) # speed =up the drawing.flower.

flower.begin_fill()

# flower.forward(200)
# flower.left(135)
# flower.forward(200)
# flower.forward(200)
# flower.left(135)
# flower.forward(200)
# flower.forward(200)
# flower.left(135)
# flower.forward(200)
# flower.forward(200)
# flower.left(135)
# flower.forward(200)
# flower.forward(200)
# flower.left(135)
# flower.forward(200)
# flower.forward(200)
# flower.left(135)
# flower.forward(200)
# flower.forward(200)
# flower.left(135)
# flower.forward(200)
# flower.forward(200)
# flower.left(135)
# flower.forward(200)

for i in range(50):
	flower.forward(200) 
	flower.left(170)


flower.end_fill()

turtle.done()