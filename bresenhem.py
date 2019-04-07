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

class Bresenham:
    '''
    Objective : To draw aline using Bresenham algorithm
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


    def drawline(self):
        '''
        Objective : To draw a line.

        Input Parameters:
             self : Implicit Parameter

        Return Value : None
        '''
        dx = p2.x - p1.x
        dy = p2.y - p1.y
        m  = dy/dx
        print(m)
        if m<1 and m>0 :
            print("1")
            p = 2*dy - dx
            x = p1.x
            y = p1.y
            xEnd = p2.x

            if p1.x > p2.x:
                x = p2.x
                y = p2.y
                xEnd = p1.x

            win.plotPixel(x,y)

            while x < xEnd:
                x = x+1
                if p <= 0:
                    p = p + 2 * dy
                else:
                    p = p + 2 * dy - 2 * dx
                    y = y+1
                win.plotPixel(x,y)
                
        elif m < 0 and m > -1:
            print("2")
            p = -2*dy - dx
            x = p1.x
            y = p1.y
            xEnd = p2.x

            if p1.x > p2.x:
                x = p2.x
                y = p2.y
                xEnd = p1.x

            win.plotPixel(x,y)

            while x < xEnd:
                x = x+1
                if p <= 0:
                    p = p - 2 * dy
                else:
                    p = p - 2 * dy - 2 * dx
                    y = y-1
                win.plotPixel(x,y)

        elif m > 1:
            print("3")
            p = 2*dx - dy
            x = p1.x
            y = p1.y
            yEnd = p2.y

            if p1.y > p2.y:
                x = p2.x
                y = p2.y
                yEnd = p1.y

            win.plotPixel(x,y)

            while y < yEnd:
                y = y+1
                if p <= 0:
                    p = p + 2 * dx
                else:
                    p = p + 2 * dx - 2 * dy
                    x = x+1
                win.plotPixel(x,y)

        elif m < -1:
            print("4")
            p = -2*dx - dy
            x = p1.x
            y = p1.y
            yEnd = p2.y

            if p1.y < p2.y:
                x = p2.x
                y = p2.y
                yEnd = p1.y

            win.plotPixel(x,y)

            while y > yEnd:
                y = y-1
                if p <= 0:
                    p = p - 2 * dx
                else:
                    p = p - 2 * dx - 2 * dy
                    x = x+1
                win.plotPixel(x,y)

if __name__=="__main__":
    win=GraphWin("Breshenham Line",1000,1000)
    p1=Point(int(input("Enter x1:")),int(input("Enter y1:")))
    p2=Point(int(input("Enter x2:")),int(input("Enter y2:")))
    Bresenham(p1,p2).drawline()     
