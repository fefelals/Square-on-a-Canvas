import turtle
import time
# creating canvas
turtle.Screen().bgcolor("yellow")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome to Turtle Window")

# turtle object creation
board = turtle.Turtle()

# creating a square
for i in range(4):
	board.forward(100)
	board.left(90)
	time.sleep(2)
	i = i+1

