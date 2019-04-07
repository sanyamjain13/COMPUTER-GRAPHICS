from graphics import *
import time

def main():

    win=GraphWin('FLying kite',1000,550)
    win.setBackground('black')

    #this is the title of the animation on the right
    title=Text(Point(820,50),'FLYING KITE')
    title.setSize(35)
    title.setStyle('bold italic')
    title.setTextColor('red')
    title.setFace("courier")
    title.draw(win)

    #this is the base of the window or the sea
    line1=Line(Point(0,520),Point(1000,520))
    line1.setWidth(40)
    line1.setFill('blue')
    line1.draw(win)

    #this is kite or the rhombus shape
    polygon=Polygon(Point(600,150),Point(700,250),Point(600,350),Point(500,250))
    polygon.draw(win)
    polygon.setFill('silver')
    polygon.setWidth(6)

    
    #tail of the kite by line2 and line3
    line2=Line(Point(600,350),Point(550,400))
    line2.draw(win)
    line2.setFill('silver')
    line2.setWidth(6)

    line3=Line(Point(600,350),Point(650,400))
    line3.draw(win)
    line3.setFill('silver')
    line3.setWidth(6)
    
    #plus(+) in the kite by line4 and line5
    line4=Line(Point(600,150),Point(600,350))
    line4.draw(win)
    line4.setWidth(6)

    line5=Line(Point(500,250),Point(700,250))
    line5.draw(win)
    line5.setWidth(6)
    
    #input text heading
    text2=Text(Point(850,470),'CLICK HERE TO FLY')
    text2.setSize(20)
    text2.setTextColor('green')
    text2.setStyle("bold")
    text2.setFace("courier")
    text2.draw(win)

    #when click on the screen it starts the paused animation
    win.getMouse()


    '''
    #input box
    entry=Entry(Point(850,400),2)
    entry.setStyle("bold italic")
    entry.setSize(20)
    entry.setTextColor('white')
    entry.draw(win)

    #when key presses it starts the animation
    win.getKey()
    '''

    
    #loops to move the kite upwards 
    y=3
    for i in range(21):
        polygon.move(11,0)
        line2.move(11,0)
        line3.move(11,0)
        line4.move(11,0)
        line5.move(11,0)
        time.sleep(0.05)

        if y==3:
            y=-5
        else:
            y=3
            
        for j in range(6):
            polygon.move(-6,y)
            line2.move(-6,y)
            line3.move(-6,y)
            line4.move(-6,y)
            line5.move(-6,y)
            time.sleep(0.1)

    time.sleep(0.8)
    #window closes after animation finishes
    win.close()               
        

main()

