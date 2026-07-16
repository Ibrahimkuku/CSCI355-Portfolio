from vpython import *
wallWidth = 10
wallTickness = .1
wallHeight= 8
wallDepth = 10
marbleRadius = .5
marble2Radius = .55

cordinateMovementX = wallWidth/2
cordinateMovementY = wallHeight/2
cordinateMovementZ = wallDepth/2

floorWall= box(color = color.white, pos = vector(0, -cordinateMovementY, 0), size = vector(wallWidth,wallTickness,wallDepth))
sleep(1)
celingWall= box(color = color.white, pos = vector(0, cordinateMovementY, 0), size = vector(wallWidth,wallTickness,wallDepth))
sleep(1)
backWall= box(color = color.white, pos = vector(0, 0, -cordinateMovementZ), size = vector(wallWidth,wallHeight,wallTickness))
sleep(1)
leftkWall= box(color = color.white, pos = vector(-cordinateMovementX, 0, 0), size = vector(wallTickness,wallHeight,wallDepth))
sleep(1)
rightWall= box(color = color.white, pos = vector(cordinateMovementX, 0, 0), size = vector(wallTickness,wallHeight,wallDepth))
sleep(1)
marble = sphere(color = color.red, radius = marbleRadius)
marble2 = sphere(color = color.green, radius = marble2Radius)


xPos = 0
yPos = 0
zPos = 0
xPosChange = .1
yPoschange = .1
zPosChange = .1


xPos2 = 2
yPos2 = 2
zPos2 = 2
xPosChange2 = .15
yPoschange2 = .15
zPosChange2 = .15

while True:
    rate(20)
    xPos += xPosChange
    yPos += yPoschange
    zPos += zPosChange
    if (xPos >= (cordinateMovementX - wallTickness/2) -marbleRadius) or (xPos <= -(cordinateMovementX - wallTickness/2 - marbleRadius)) :
        xPosChange *=(-1)
    if(yPos >= (cordinateMovementY - wallTickness/2) -marbleRadius) or (yPos <= -(cordinateMovementY - wallTickness/2 - marbleRadius)):
        yPoschange *= -1
    if(zPos >= (cordinateMovementZ - wallTickness/2) -marbleRadius) or (zPos <= -(cordinateMovementZ - wallTickness/2 - marbleRadius)):
        zPosChange *= -1
    marble.pos = vector(xPos, yPos, zPos)
    
    xPos2 += xPosChange2
    yPos2 += yPoschange2
    zPos2 += zPosChange2
    if (xPos2 >= (cordinateMovementX - wallTickness/2) -marble2Radius) or (xPos2 <= -(cordinateMovementX - wallTickness/2 - marble2Radius)):
        xPosChange2 *=(-1)
    if(yPos2 >= (cordinateMovementY - wallTickness/2) -marble2Radius) or (yPos2 <= -(cordinateMovementY - wallTickness/2 - marble2Radius)):
        yPoschange2 *= -1
    if(zPos2 >= (cordinateMovementZ - wallTickness/2) -marble2Radius) or (zPos2 <= -(cordinateMovementZ - wallTickness/2 - marble2Radius)):
        zPosChange2 *= -1
    marble2.pos = vector(xPos2, yPos2, zPos2) 

