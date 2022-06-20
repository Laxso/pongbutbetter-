#Game Screen 
game = Group(Rect(0,0,400,400, fill ='black'),
Line(200,0,200,400, lineWidth=10,dashes=True,fill='white')

)

#Title screen
TitleScreen = Group(Rect(0,0,400,400,fill='black'),
Label('PONG',200,200,fill='White',size=120,bold=True),
Label('press r to start',200,300,fill='gray',size=15,bold=True),
Label('-player one-',200,320,fill='gray',size=15,bold=True),
Label('(w) to go up and (s) to go down',200,340,fill='gray',size=15,bold=True),
Label('-player two-',200,360,fill='gray',size=15,bold=True),
Label('(up key) to go up amd (down key ) to go down',200,380,fill='gray',size=15,bold=True),

)

#score label
LS = Label(0,160,40,fill='white',size=55,visible=False)
RS = Label(0,260,40,fill='white',size=55,visible=False)

#Ball Label
ball= Rect(200,200,10,10,fill='white',visible=False)

#player1 label

player1 = Rect(40,160,15,65,fill='white',visible= False)

#player2 label

player2 = Rect(360,160,15,65,fill='white',visible= False)

#key player commands
def onKeyHold(keys):

    if ( 'w' in keys):
        player.centerY += -20
    
    if( 's' in keys):
        player.centerY += +20
    
    if ( 'up' in keys):
        player.centerY += -20
    
    if( 'down' in keys):
        player.centerY +=  20

#key visible commands
def onKeyPress(keys):
    
    if('r' in keys):
        
        
        TitleScreen.visible=False
        
        LS.visible=True
        RS.visible=True

        Ball.visible = True

        player1.visible = True

        player2.visible = True

#balls og speed 
app.stepsPerSecond = 20
ball.dx = 10
ball.dy = 5

#Ball Bounce
def onStep():
    ball.centerX += ball.dx
    ball.centerY -= ball.dy


    if(ball.hitsShape(player2) == True):
        ball.dx = -ball.dx
        ball.dy = -ball.dy
        app.stepsPerSecond += 1
    
    if (ball.hitsShape(player) == True):
        ball.dx = -ball.dx
        ball.dy = +ball.dy
        app.stepsPerSecond += 1

#ballReset
    if((ball.left < 0) or (ball.right > 400)):
        ball.centerX = 200
        ball.centerY = 200
        ball.dx = -ball.dx
        app.stepsPerSecond = 30
        ball.dx = 10
#score

    if(ball.centerX <= 20):
        RS.value += .50
    elif (ball.centerX >=380):
        LS.value += .50