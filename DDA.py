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

class DDA:
    '''
    Objective : To draw aline using DDA algorithm
    '''

    def __init__(self,p1,p2):
        '''
        Objective : To initialize endpoints of a line.

        Input Parameters:
             self : Implicit Parameter
               p1 : Initial point of line
               p2 : End point of line

        Return Value : None
        '''

        self.p1 = p1
        self.p2 = p2


    def dda(self):
        '''
        Objective : To draw a line.

        Input Parameters:
             self : Implicit Parameter

        Return Value : None
        '''
        dx = p2.x - p1.x
        dy = p2.y - p1.y
        xInc,yInc,steps = 0,0,0
        x = p1.x
        y = p1.y
        
        if abs(dx)>abs(dy):
            steps = abs(dx)
        else:
            steps = abs(dy)
            
        xInc = dx/steps
        yInc = dy/steps
        win.plotPixel(x,y,'red')
        
        for i in range(steps):
            x += xInc
            y += yInc
            win.plotPixel(x,y,'red')
        

if __name__=="__main__":
    win=GraphWin("DDA Line",1000,1000)
    p1=Point(int(input("Enter x1:")),int(input("Enter y1:")))
    p2=Point(int(input("Enter x2:")),int(input("Enter y2:")))
    DDA(p1,p2).dda()     
