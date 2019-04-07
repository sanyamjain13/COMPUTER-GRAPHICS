from graphics import *

class vertex:

    def __init__(self,x,y):

        self.x=x
        self.y=y

class liang_barskey:

    def __init__(self):

        self.xmin=None
        self.ymin=None
        self.xmax=None
        self.ymax=None
        self.p=[]
        self.q=[]
        self.end_pts=[]
        self.t1=0
        self.t2=1


    def input_window(self):

        print('ENTER WINDOW COORDINATES BY GIVING SPACES: \n')
        xmin,ymin,xmax,ymax=list(map(int,input('[XMIN , YMIN , XMAX , YMAX] : ').split()))
        self.xmin=xmin
        self.ymin=ymin
        self.xmax=xmax
        self.ymax=ymax

        print('XMIN: '+str(self.xmin)+'\n'+'YMIN: '+str(self.ymin)+'\n'+'XMAX: '+str(self.xmax)+'\n'+'YMAX: '+str(self.ymax))

    def end_points(self):
        
        for i in range(1,3):
            x,y=list(map(int,input('ENTER X'+str(i)+' & Y'+str(i)+' COORDINATE OF LINE: ').split()))
            self.end_pts.append(vertex(x,y))

        for j in range(len(self.end_pts)):
            v=self.end_pts[j]
            print('Vertex-'+str(j+1),': (',v.x,',',v.y,')')

    def line_parameters(self):
        point1=self.end_pts[0]
        point2=self.end_pts[1]

        p1=-(point2.x-point1.x) #-(delta x)
        p2=(point2.x-point1.x)  #(delta x)
        p3=-(point2.y-point1.y) #-(delta y)
        p4=(point2.y-point1.y)  #(delta y)
        self.p=[p1,p2,p3,p4] #list of Pk
        print('P-> ',self.p)

        q1=point1.x-self.xmin #q1=x1-xmin
        q2=self.xmax-point1.x #q2=xmax-x1
        q3=point1.y-self.ymin #q3=y1-ymin
        q4=self.ymax-point1.y #q4=ymax-y1
        self.q=[q1,q2,q3,q4] #list of Qk
        print('Q-> ',self.q)

        for i in range(len(self.p)):
            try:
                t=float(self.q[i]/self.p[i]) #(t= Qk/Pk)
            except ZeroDivisionError as err:
                print('-------DIVISION BY ZERO OCCURED --------- \n')

            # t should be (0<= t <= 1), if not we will discard 
            if(t<0 or t>1):
                continue
            else:
                #if p is negative then take the corresponding t and find max(0,t)
                if(self.p[i]<0):
                    self.t1=max(self.t1,t)

                #if p is positive find corresponding t and find min(1,t)
                else:
                    self.t2=min(self.t2,t)

        print('t1 = ',round(self.t1,2),'AND','t2 = ',round(self.t2,2))
                    

    def clip_line(self):

        p1=self.end_pts[0] #points of end point 1 of line
        p2=self.end_pts[1] #points of end point 2 of line

        #if t2-t1<0 then line will be rejected
        if(self.t1 > self.t2):
            print('LINE REJECTED')

        #else we will find the intersecting points of clipped line first with t1 and again with t2
        else:
            x1=p1.x+self.t1*(p2.x-p1.x)
            y1=p1.y+self.t1*(p2.y-p1.y)

            x2=p1.x+self.t2*(p2.x-p1.x)
            y2=p1.y+self.t2*(p2.y-p1.y)


        '''
        To find new Points -
        x=x1+t1(x2-x1)
        y=y1+t1(y2-y1)
        
        '''
        print('END POINTS OF FINAL CLIPPED LINE ARE: \n')
        
        print('POINTS WITH t1 : ')
        print('x1 =',x1)
        print('y1 =',y1)

        print('\n')

        print('POINTS WITH t2')
        print('x2 =',x2)
        print('y2 =',y2)

        return[[x1,y1],[x2,y2]]

    def draw_figure(self):

        win=GraphWin('Liang-Barskey',500,500)
        x_half=win.getWidth()/2
        y_half=win.getHeight()/2
        win.setBackground('black')

        
        #original line
        v1=self.end_pts[0]
        v2=self.end_pts[1]

        #final clipped line
        final=self.clip_line()
        v3=final[0]
        v4=final[1]

        #window of figure
        window=Rectangle(Point(self.xmin+x_half,y_half-self.ymin),Point(self.xmax+x_half,y_half-self.ymax))
        window.setOutline('white')
        window.draw(win)

        #drawing of original line,clipped line and shifted axis
        initial_line=Line(Point(v1.x+x_half,y_half-v1.y),Point(v2.x+x_half,y_half-v2.y))
        initial_line.draw(win)
        initial_line.setFill('yellow')

        final_line=Line(Point(v3[0]+x_half,y_half-v3[1]),Point(v4[0]+x_half,y_half-v4[1]))
        final_line.setFill('green')
        final_line.draw(win)
        final_line.setWidth(6)

        
        #axis            
        line=Line(Point(0,y_half),Point(500,y_half))
        line.draw(win)
        line.setFill('white')
        line.setWidth(2)
        
        line2=Line(Point(x_half,0),Point(x_half,500))
        line2.setFill('white')
        line2.draw(win)
        line2.setWidth(2)
    
def main():

    l=liang_barskey()
    
    print('--------------------------------------------- \n')
    l.input_window()
    print('--------------------------------------------- \n')
    l.end_points()
    print('--------------------------------------------- \n')
    l.line_parameters()
    print('--------------------------------------------- \n')
    l.clip_line()
    print('--------------------------------------------- \n')

    l.draw_figure()
if __name__=='__main__':
    main()
        
