from vpython import *
from threading import*

mRadius=2
wallThickness=.1
roomWidth=10
roomDepth=10
roomHeight=30
floor=box(pos=vector(0,-roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth), color=color.white)
ceiling=box(pos=vector(0,roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth), color=color.white)
backWall=box(pos=vector(0,0,-roomDepth/2),size=vector(roomWidth,roomHeight,wallThickness), color=color.white)
leftWall=box(pos=vector(-roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth), color=color.white)
rightWall=box(pos=vector(roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth), color=color.white)
marble=sphere(radius=mRadius,color=color.red)
deltaX=.1
deltaY= .1
deltaZ= .1
xPos =0
yPos =1
zPos =-1


while True:
    rate(50)
    xPos += deltaX
    yPos+=deltaY
    zPos+=deltaZ
    
    if (xPos>=(((roomWidth/2)-mRadius)-wallThickness/2) or xPos<=-(((roomWidth/2)-mRadius)-wallThickness/2)):
        deltaX=deltaX*(-1)
    marble.pos=vector(xPos,0,0)