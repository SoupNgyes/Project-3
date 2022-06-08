import turtle

turtle.bgcolor("white")
turtle.setup (600, 600)
turtle.shape ("turtle")

screen = turtle.Screen()
kaia = turtle.Turtle()



def star(color, length):
  kaia.fillcolor(color)
  kaia.begin_fill()
  
  corners = 0
  while corners < 5:
    kaia.forward(length)
    kaia.right(144)
    corners +=1
  
  kaia.end_fill()


def triangle(color, length):
  kaia.fillcolor(color)
  kaia.begin_fill()
  
  corners = 0
  while corners < 3:
    kaia.forward(length)
    kaia.right(120)
    corners +=1
  
  kaia.end_fill()

def circle(color, length):
  kaia.fillcolor(color)
  kaia.begin_fill()
  
  kaia.circle(length)

  kaia.end_fill()



  

def square(color,length):

shape = input("Give me a shape: ")
color = input("Give me a color: ")
length = int(input("Give me a length: "))

if shape == "star":
  star(color, length)
elif shape == "triangle":
  triangle(color, length)
elif shape == "circle":
  circle(color, length)
elif shape == "square":
  square(color, length)