# from vpython import *
# from time import *
# firstVisual = cylinder(color= color.yellow,length=12,radius=1)
# sleep(5)
# firstVisual.color=color.green

from vpython import *

# wall = box(color=color.green, size=vector(10, 0.1, 10))
# sleep(5)
# shape= sphere(color=color.red)
# sleep(3)
# shape3=arrow(color=color.blue, size=vector(-10,1,-10))
# hw. create a 3d room with a red marble at the center.

floorwall = box(color=color.white, pos=vector(0,-5,0),size=vector(15,0.2,30))
sleep(2)
celingwall = box(color=color.white, pos=vector(0,5,0),size=vector(15,0.2,30))
sleep(2)
leftwall = box(color=color.white, pos=vector(-7.6,0,0),size=vector(.2,10.5,30))
sleep(2)
rightwall = box(color=color.white, pos=vector(7.6,0,0),size=vector(.2,10.5,30))  
sleep(2)
backwall = box(color=color.yellow, pos=vector(0,0,-15),size=vector(15,10,0.2)) 
sleep(2)
marble=sphere(color=color.red, radius=.7)

movement = 0.1
xPos = 0
trackRightWall = 6.8
trackLeftWall = -6.8
speed = 50

while True:
    
    rate(speed)
    xPos += movement 
    marble.pos = vector(xPos, 0, 0)
    
    if marble.pos.x >= trackRightWall or marble.pos.x <= trackLeftWall:
        movement *= -1  
        xPos = 2 * min(trackRightWall, max(trackLeftWall, xPos)) - xPos
    if speed>=500:
        speed =500
    speed += .5
    