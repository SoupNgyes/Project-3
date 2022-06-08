import turtle

turtle.bgcolor("lightgreen")
turtle.setup (600, 600)
turtle.shape ("turtle")

screen = turtle.Screen()
bob = turtle.Turtle()

#color = input("Give me a color: ")
#length = input("Give me a length: ")

def star():
    print("star")
  def triangle():
    print("triangle")
  def circle():
    print("circle")


shape = input("Give me a shape: ")

if shape == "star":
  star()
elif shape == "triangle":
  triangle()
elif shape == "circle":
  circle()
