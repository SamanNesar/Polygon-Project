import turtle 
t = turtle.Turtle()
window = turtle.Screen()

t.color("red" , "green")
window.bgcolor("light green")
window.title("Sam Poly Project")

sideofpoly = int(input("Enter the no of the sides of the polygon : "))


length = int(input("Enter the length of the sides of the polygon : "))


for _ in range(sideofpoly):
	turtle.forward(length)
	turtle.right(360 / sideofpoly)

input()
