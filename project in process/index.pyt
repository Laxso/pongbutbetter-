

#rectangle summon commands
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

#Game Screen

game = turtle.Turtle()
draw_rectangle (0,0,400,400, fill ='black'),

#line commands


from turtle import *
import turtle
 
tur = turtle.Turtle()
tur.hideturtle()
 
turtle.done()

def drawdot(space,x):
  for i in range(x):
    for j in range(x):
        

        tur.dot()
          

       

   
    tur.down()
    goto(0,300)
    
    tur.down()
    goto(0,-300)
    
  

tur.penup()
drawdot(900,1)
  

tur.hideturtle()

turtle.done()

#Title screen
TitleScreen = turtle.Turtle()
(draw_rectangle(0,0,400,400,fill='black'),
Label('PONG',200,200,fill='White',size=120,bold=True),
Label('press r to start',200,300,fill='gray',size=15,bold=True),
Label('-player one-',200,320,fill='gray',size=15,bold=True),
Label('(w) to go up and (s) to go down',200,340,fill='gray',size=15,bold=True),
Label('-player two-',200,360,fill='gray',size=15,bold=True),
Label('(up key) to go up amd (down key ) to go down',200,380,fill='gray',size=15,bold=True),

)
turtle.done()


#score label
LS = Label(0,160,40,fill='white',size=55,visible=False)
RS = Label(0,260,40,fill='white',size=55,visible=False)

#Ball Label

Ball= turtle.Turtle()
draw_rectangle(200,200,10,10,fill='white',visible=False)

turtle.done()
#player1 label


PLayer1= turtle.Turtle()
draw_rectangle(40,160,15,65,fill='white',visible= False)

turtle.done()

#player2 label


Player2= turtle.Turtle()
draw_rectangle(360,160,15,65,fill='white',visible= False)
turtle.done()
#key player commands
def onKeyHold(keys):

    if ( 'w' in keys):
        PLayer1.centerY += -20
    
    if( 's' in keys):
        PLayer1.centerY += +20
    
    if ( 'up' in keys):
        Player2.centerY += -20
    
    if( 'down' in keys):
        Player2.centerY +=  20

#key visible commands
def onKeyPress(keys):
    
    if('r' in keys):
        
        
        TitleScreen.visible=False
        
        LS.visible=True
        RS.visible=True

        Ball.visible = True

        PLayer1.visible = True

        Player2.visible = True

#balls og speed 
Ball.stepsPerSecond = 20
Ball.dx = 10
Ball.dy = 5

#Ball Bounce
def onStep():
    Ball.centerX += Ball.dx
    Ball.centerY -= Ball.dy


    if(Ball.hitsShape(Player2) == True):
        Ball.dx = -Ball.dx
        Ball.dy = -Ball.dy
        Ball.stepsPerSecond += 1
    
    if (Ball.hitsShape(PLayer1) == True):
        Ball.dx = -Ball.dx
        Ball.dy = +Ball.dy
        Ball.stepsPerSecond += 1

#ballReset
    if((Ball.left < 0) or (Ball.right > 400)):
        Ball.centerX = 200
        Ball.centerY = 200
        Ball.dx = -Ball.dx
        Ball.stepsPerSecond = 30
        Ball.dx = 10
#score

    if(Ball.centerX <= 20):
        RS.value += .50
    elif (Ball.centerX >=380):
        LS.value += .50