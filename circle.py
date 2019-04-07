from graphics import *

class Point:
    '''
    Objective : To represent a point in 2D plane
    '''

    def __init__(self,x,y):
        '''
        Objective : To initialize a Point object

        Input Parameters:
              self : Implicit Parameter
                 x : X-coordinate
                 y : Y-coordinate

        Return Value : None
        '''
        self.x = x
        self.y = y

    
class Circle:
    '''
    Objective : To draw a circle using mid point algorithm
    '''

    def __init__(self,r,c):
        '''
        Objective : To initialize the center and radius of a circle

        Input Parameters:
              self : Implicit Parameter
                 r : Radius of circle
                 c : Center coordinate of circle

        Return Value : None 
        '''

        self.r = r
        self.c = c

    def putPixels(self,p):
        '''
        Objective : To draw all eight symmetric points of a coordinate

        Input Parameters:
              self : Implicit Parameter
                 p : A coordinate of circle

        Return Value : None         
        '''

        win.plotPixel(self.c.x + p.x,self.c.y + p.y,"red")
        win.plotPixel(self.c.x - p.x,self.c.y + p.y,"blue")
        win.plotPixel(self.c.x + p.x,self.c.y - p.y,"green")
        win.plotPixel(self.c.x - p.x,self.c.y - p.y,"yellow")
        win.plotPixel(self.c.x + p.y,self.c.y + p.x,"red")
        win.plotPixel(self.c.x - p.y,self.c.y + p.x,"blue")
        win.plotPixel(self.c.x + p.y,self.c.y - p.x,"green")
        win.plotPixel(self.c.x - p.y,self.c.y - p.x,"yellow")

    def drawCircle(self):
        '''
        Objective : To draw a circle with given radius and center point

        Input Parameters:
              self : Implicit Parameter

        Return Value : None
        '''
        x = 0
        y = self.r
        p = 1 - self.r
        xInc,yInc = 0,0

        self.putPixels(Point(x,y))
        
        while x < y:

            x += 1

            if p <= 0:
                p += 2 * x + 1
            else:
                y -= 1
                p += 2 * (x -y) + 1

            self.putPixels(Point(x,y))
            
                
if __name__ == "__main__" :

    win = GraphWin("Circle",1000,1000)
    r = int(input("Enter the radius of circle:"))
    c = Point(int(input("Enter the center coordinate:\n Enter x-coordinate:")),int(input(" Enter y-coordinate:")))
    for i in range(1,r+1):
        Circle(i,c).drawCircle()
