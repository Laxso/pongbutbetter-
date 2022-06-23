import turtle
t = turtle.Turtle()
def draw_rectangle(length, height):
    for i in range(0,4):
        if i % 2 == 0: 
            t.forward(length)
            t.right(90)
        else: 
            t.forward(height)
            t.right(90)
draw_rectangle(100, 200)

from turtle import *
import turtle 
 
tur = turtle.Turtle()
#------------------------------------------------------------------------------------

from turtle import *
import turtle
 
tur = turtle.Turtle()
tur.fillcolor('cyan')

tur.forward(150)
 
turtle.done()

def drawdot(space,x):
  for i in range(x):
    for j in range(x):
        

        tur.dot()
          

        tur.forward(space)
    tur.backward(space*x)
      

    tur.right(90)
    tur.forward(space)
    tur.left(90)
  

tur.penup()
drawdot(10,8)
  

tur.hideturtle()