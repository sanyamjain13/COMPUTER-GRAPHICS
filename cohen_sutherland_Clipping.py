from graphics import *

INSIDE=0
LEFT=1
RIGHT=2
BOTTOM=4
TOP=8

def compute_code(x,y,xmin,ymin,xmax,ymax):
    code=""
    left=x-xmin
    right=xmax-x
    bottom=y-ymin
    top=ymax-y

    
    if(top<0):
        code+="1"
    else:    
        code+="0"

    
    if(bottom<0):
        code+="1"
    else:
        code+="0"

    
    if(right<0):
        code+="1"
    else:
        code+="0"
    
    if(left<0):
        code+="1"
    else:
        code+="0"

    #converting binary string into decimal integer number (TBRL-top bottom right left)    
    return int(code,2)

def cohenSutherland(x1,y1,x2,y2,xmin,ymin,xmax,ymax):

    code1=compute_code(x1,y1,xmin,ymin,xmax,ymax)
    code2=compute_code(x2,y2,xmin,ymin,xmax,ymax)
    
    accept=False

    while True:

        '''
        if both the points are inside then we will accept the line
        '''
        if code1==0 and code2==0:
            accept= True
            break

        '''
        if both the points are outside then we will reject the line
        '''
        elif (code1 & code2)!=0:
            break


        '''
        if the line is partially inside and outside
        '''
        
        else:
            #slope
            m=float((y2-y1)/(x2-x1))

            #inverse of slope
            m_inv=float((x2-x1)/(y2-y1))
            
            if code1!=0:
                code_examine=code1
            else:
                code_examine=code2

            
            #if non-zero integer value then true, otherwise the conditions wont run
            if code_examine & TOP:
                y=ymax
                x=((ymax-y1)*m_inv)+x1
                print('INTERSECTION WITH TOP: ',x,',',y)


            elif code_examine & BOTTOM:
                y=ymin
                x=((ymin-y1)*(m_inv))+x1
                print('INTERSECTION WITH BOTTOM: ',x,',',y)


            elif code_examine & RIGHT:
                y=y1+((m)*(xmax-x1))
                x=xmax
                print('INTERSECTION WITH RIGHT: ',x,',',y)


            elif code_examine & LEFT:
                y=y1+((m)*(xmin-x1))
                x=xmin
                print('INTERSECTION WITH LEFT: ',x,',',y)


            #changing of the end points to intersection points found
            if code_examine==code1:
                x1=x
                y1=y
                code1=compute_code(x1,y1,xmin,ymin,xmax,ymax)

            else:
                x2=x
                y2=y
                code2=compute_code(x2,y2,xmin,ymin,xmax,ymax)

    if accept:
        print('\n-----------------------------------------------------')
        print("LINE ACCEPTED FROM : ",'(',x1,',',y1,')'," To ",'(',x2,',',y2,')')
        return [x1,y1,x2,y2]
        
    else:
        print("line rejected")
        return None


def main():
    print("ENTER WINDOW DIMENSIONS BY GIVING SPACE ->\n")
    xmin,ymin,xmax,ymax=[int(x) for x in input("ENTER : XMIN,YMIN,XMAX,YMAX : ").split()]
    print('xmin='+str(xmin),' ,','ymin='+str(ymin),' ,','xmax='+str(xmax),' ,','ymax='+str(ymax))
    print('----------------------------')

    print("ENTER LINE END POINTS BY GIVING SPACE ->\n")
    x1,y1,x2,y2=list(map(int ,input('ENTER X1,Y1,X2,Y2 : ').split()))
    endpt_1='x1= '+str(x1)+' , '+'y1= '+str(y1)
    endpt_2='x2= '+str(x2)+' , '+'y2= '+str(y2)
    
    print(endpt_1,'&',endpt_2)
    print('----------------------------')

    lst=cohenSutherland(x1,y1,x2,y2,xmin,ymin,xmax,ymax)
    

##    win=GraphWin('cohen',800,800)
##    line1=Line(Point(xmin,ymin),Point(xmax,ymin))
##    line1.draw(win)
##
##    line2=Line(Point(xmin,ymin),Point(xmin,ymax))
##    line2.draw(win)
##
##    line3=Line(Point(xmin,ymax),Point(xmax,ymax))
##    line3.draw(win)
##    
##    line4=Line(Point(xmax,ymin),Point(xmax,ymax))
##    line4.draw(win)
##
##    line5=Line(Point(x1,y1),Point(x2,y2))
##    line5.draw(win)
##
##    line6=Line(Point(x11,y11),Point(x22,y22))
##    line6.draw(win)

if __name__=='__main__':
    main()

    

