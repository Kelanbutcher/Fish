xCoordinate=random(50,200)
yCoordinate=random(50,200)
xspeed=4
ySpeed=9

def setup():
    size(500,500)
    background(0,0,255)
    fish(200,100,70,50)
    
    
    

def fish(xCoordinate, yCoordinate,fishWidth,fishHeight):
    
    
    
    noStroke()
    fill(100,200,0)
    
    ellipse(xCoordinate, yCoordinate,fishWidth,fishHeight)
    noStroke()
    triangle(225, 101, 265, 121, 265, 76)

    ellipse(xCoordinate+50, yCoordinate+50,fishWidth/2,fishHeight/2)
    triangle(
    
def draw ():
    global xCoordinate
    xCoordinate+= 1
     

    
