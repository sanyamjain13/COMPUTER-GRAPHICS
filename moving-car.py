from graphics import *
win=GraphWin('Car-MOving',800,800)

road=Rectangle(Point(0,500),Point(800,600)) #END POINTS OF DIAGONALS
road.draw(win)
road.setFill('grey')

for i in range(30,800,100):
    dashes=Line(Point(i,550),Point(i+40,550))
    dashes.draw(win)
    dashes.setFill("yellow")
    dashes.setWidth(5)

#CAR MAKING

line1=Line(Point(100,350),Point(250,350))
line1.draw(win)
line1.setWidth(3)

line2=Line(Point(250,350),Point(350,400))
line2.draw(win)
line2.setWidth(3)

line3=Line(Point(350,400),Point(350,450))
line3.draw(win)
line3.setWidth(3)

line4=Line(Point(350,450),Point(100,450))
line4.draw(win)
line4.setWidth(3)

line5=Line(Point(100,450),Point(100,350))
line5.draw(win)
line5.setWidth(3)

tyre1 = Oval(Point(150, 450), Point(200, 500)) # set corners of bounding box
tyre1.setFill("black")
tyre1.draw(win)

tyre2 = Oval(Point(250, 450), Point(300, 500)) # set corners of bounding box
tyre2.setFill("black")
tyre2.draw(win)

window1=Rectangle(Point(110,360),Point(250,400)) #END POINTS OF DIAGONALS
window1.draw(win)
window1.setFill('black')

for i in range(100,300,5):
    for j in range(1000000):
        pass
    line1.move(10,0)
    line2.move(10,0)
    line3.move(10,0)
    line4.move(10,0)
    line5.move(10,0)
    tyre1.move(10,0)
    tyre2.move(10,0)
    window1.move(10,0)
