from graphics import *

win=GraphWin("scenery",800,600)
win.setBackground('light blue')

mountains=Polygon(Point(0,150),Point(100,0),Point(200,150),Point(300,0),Point(400,150),Point(500,0),Point(600,150),Point(700,0),Point(800,150))
mountains.setWidth(4)
mountains.setFill('brown')
mountains.setOutline('brown')
mountains.draw(win)

sun=Circle(Point(400,53),51)
sun.setWidth(7)
sun.setOutline('yellow')
sun.setFill('orange')
sun.draw(win)


house_name=Text(Point(220,250),'MANNAT')
house_name.setSize(25)
house_name.setFace('courier')
house_name.setStyle('bold')
house_name.draw(win)

triangle=Polygon(Point(50,300),Point(100,200),Point(150,300))
triangle.draw(win)
triangle.setWidth(3)
triangle.setFill('silver')
triangle.setOutline('grey')

oval=Oval(Point(80,240),Point(120,280))
oval.draw(win)
oval.setOutline('grey')
oval.setWidth(3)

roof=Polygon(Point(100,200),Point(300,200),Point(350,300),Point(150,300))
roof.setWidth(3)
roof.draw(win)
roof.setFill('silver')
roof.setOutline('grey')

front_of_house=Polygon(Point(150,300),Point(350,300),Point(350,450),Point(150,450))
front_of_house.draw(win)
front_of_house.setWidth(3)
front_of_house.setOutline('grey')
front_of_house.setFill('silver')

main_gate=Rectangle(Point(50,300),Point(150,450))
main_gate.draw(win)
main_gate.setWidth(3)
main_gate.setFill('silver')
main_gate.setOutline('grey')

gate=Rectangle(Point(80,350),Point(120,450))
gate.setWidth(3)
gate.draw(win)
gate.setOutline('grey')
gate.setFill('grey')

grass=Rectangle(Point(0,450),Point(800,600))
grass.setOutline('light green')
grass.setFill('light green')
grass.draw(win)

##myImage = Image(Point(500,350), "man.gif")
##myImage.draw(win)
##win.mainloop()





