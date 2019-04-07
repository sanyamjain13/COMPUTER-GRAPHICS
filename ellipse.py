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

    
class Ellipse:
    '''
    Objective : To draw a ellipse using mid point algorithm
    '''

    def __init__(self,rx,ry,c):
        '''
        Objective : To initialize the center and radii of a ellipse

        Input Parameters:
              self : Implicit Parameter
                rx : X-Radius of ellipse
                ry : Y-Radius of ellipse
                 c : Center coordinate of ellipse

        Return Value : None 
        '''

        self.rx = rx
        self.ry = ry
        self.c = c

    def putPixels(self,p):
        '''
        Objective : To draw all four symmetric points of a coordinate

        Input Parameters:
              self : Implicit Parameter
                 p : A coordinate of ellipse

        Return Value : None         
        '''

        win.plotPixel(self.c.x + p.x,self.c.y + p.y,"red")
        win.plotPixel(self.c.x - p.x,self.c.y + p.y,"blue")
        win.plotPixel(self.c.x + p.x,self.c.y - p.y,"green")
        win.plotPixel(self.c.x - p.x,self.c.y - p.y,"yellow")

      
    def drawEllipse(self):
        '''
        Objective : To draw a ellipse with given radius and center point

        Input Parameters:
              self : Implicit Parameter

        Return Value : None
        '''
        x = 0
        y = self.ry
        p1 = self.ry ** 2 - ( self.rx ** 2 * self.ry ) + ( 0.25 * rx ** 2)
        dx = 2 * (self.ry ** 2) * x
        dy = 2 * (self.rx ** 2) * y

        while True:
            self.putPixels(Point(x,y))
            x += 1

            if p1<0:
                dx = dx + 2 * (self.ry ** 2)
                p1 = p1 + dx + self.ry ** 2
            else:
                y -= 1
                dx = dx + 2 * (self.ry ** 2)
                dy = dy - 2 * (self.rx ** 2)
                p1 = p1 + dx - dy + self.ry ** 2

            if dx >= dy :
                break

        p2 = ((self.ry ** 2) * ( x+0.5 )**2) + (self.rx ** 2 * (y-1)**2) - (self.rx ** 2 * self.ry**2)
        while True:
            self.putPixels(Point(x,y))
            y -= 1

            if p2 > 0:
                dy = dy - 2 * self.rx ** 2
                p2 = p2 - dy + self.rx ** 2
            else:
                x += 1
                dy = dy - 2 * self.rx ** 2
                dx = dx + 2 * self.ry ** 2
                p2 = p2 + dx - dy + self.rx ** 2

            if y<=0:
                break
                
if __name__ == "__main__" :

    win = GraphWin("Circle",1000,1000)
    rx,ry = int(input("Enter the radii of ellipse:\n Enter x-radius:")),int(input(" Enter y-radius:"))
    c = Point(int(input("Enter the center coordinate:\n Enter x-coordinate:")),int(input(" Enter y-coordinate:")))
    #for i in range(1,r+1):
    Ellipse(rx,ry,c).drawEllipse()

