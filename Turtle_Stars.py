import turtle

#Recursive function

star = turtle.Turtle()

star.getscreen().bgcolor("#994444") #color code

star.speed(10)


# star.forward(200)
# star.left(216)
# star.forward(200)
# star.left(216)
# star.forward(200)
# star.left(216)
# star.forward(200)
# star.left(216)
# star.forward(200)
# star.left(216)

# for i in range(5)
# 	star.forward(200)
# 	star.left(216)

def star_recursive(turtle, size):
	if size <= 10:
		return
	else:
		for i in range(5):
			turtle.forward(size)
			star_recursive(turtle,size/3)
			turtle.left(216)

star_recursive(star, 200)





turtle.done()