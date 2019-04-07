from graphics import *

class vertex:

    def __init__(self,x,y):

        self.x=x
        self.y=y

class sutherland_clip:

    def __init__(self):

        self.xmin=None
        self.ymin=None
        self.xmax=None
        self.ymmax=None
        self.n=None
        self.polygon_nodes=[]
        self.initial_figure=[]

    def input(self):

        print('COORDINATES OF WINDOW =>')
        self.xmin=int(input('ENTER XMIN OF WINDOW : '))
        self.ymin=int(input('ENTER YMIN OF WINDOW : '))
        self.xmax=int(input('ENTER XMAX OF WINDOW : '))
        self.ymax=int(input('ENTER YMAX OF WINDOW : '))
        print('\n')

        self.n=int(input('ENTER NUMBER OF NODES/VERTICES IN POLYGON : '))
        print('\n')
        
        for i in range(1,self.n+1):
            print('NODE:'+str(i)+'--')
            x=int(input('ENTER X COORDINATE OF NODE:'+str(i)+'-> '))
            y=int(input('ENTER Y COORDINATE OF NODE:'+str(i)+'-> '))
            print('------------------------------------------ \n')
            self.polygon_nodes.append(vertex(x,y))

        self.initial_figure=self.polygon_nodes

    def left(self):

        new_output_lst=[]
        n=self.n
        for i in range(self.n):
            '''
            we have used modulo for second vertex index so that when it reaches
            the end vertex, then it can be connected to the first vertex
            '''
            
            #if both vertices are outside, then do nothing
            if(self.polygon_nodes[i].x < self.xmin and self.polygon_nodes[(i+1)%n].x < self.xmin):
                continue

            #both vertices are inside, save the second vertex
            if(self.polygon_nodes[i].x > self.xmin and self.polygon_nodes[(i+1)%n].x > self.xmin):
                x=self.polygon_nodes[(i+1)%n].x
                y=self.polygon_nodes[(i+1)%n].y
                new_output_lst.append(vertex(x,y))

            #if vertex 1 is outside and vertex 2 is inside, save intersection and 2nd point
            if(self.polygon_nodes[i].x < self.xmin and self.polygon_nodes[(i+1)%n].x> self.xmin):
                #m=y2-y1/x2-x1
                m=float((self.polygon_nodes[(i+1)%n].y-self.polygon_nodes[i].y)/(self.polygon_nodes[(i+1)%n].x-self.polygon_nodes[i].x))
                m=round(m,2)
                #intersecting points: [x=xmin, y=y1+m(xmin-x1)]
                x_int=self.xmin
                y_int=round(m*(x_int-self.polygon_nodes[i].x)+self.polygon_nodes[i].y,2)
                new_output_lst.append(vertex(x_int,y_int))

                #another point is the vertex-2
                x=self.polygon_nodes[(i+1)%n].x
                y=self.polygon_nodes[(i+1)%n].y
                new_output_lst.append(vertex(x,y))
                

            #if vertex 1 is inside and vertex 2 is outside, then save the intersecting point only
            if(self.polygon_nodes[i].x>self.xmin and self.polygon_nodes[(i+1)%n].x<self.xmin):
                #m=y2-y1/x2-x1
                m=float((self.polygon_nodes[(i+1)%n].y-self.polygon_nodes[i].y)/(self.polygon_nodes[(i+1)%n].x-self.polygon_nodes[i].x))
                m=round(m,2)
                #intersecting points: [x=xmin, y=y1+m(xmin-x1)]
                x_int=self.xmin
                y_int=round(m*(x_int-self.polygon_nodes[i].x)+self.polygon_nodes[i].y,2)
                new_output_lst.append(vertex(x_int,y_int))
                

        self.n=len(new_output_lst)
        self.polygon_nodes=new_output_lst
        #self.remove_duplicate()

    def top(self):

        new_output_lst=[]
        n=self.n

        for i in range(n):

            #if both the vertices are outside the top edge
            if(self.polygon_nodes[i].y>self.ymax and self.polygon_nodes[(i+1)%n].y>self.ymax):
                continue

            #both vertices are inside, save the second vertex
            if(self.polygon_nodes[i].y <=self.ymax and self.polygon_nodes[(i+1)%n].y <=self.ymax):
                x=self.polygon_nodes[(i+1)%n].x
                y=self.polygon_nodes[(i+1)%n].y
                new_output_lst.append(vertex(x,y))

            #if vertex 1 is outside and vertex 2 is inside, save intersection and 2nd point
            if(self.polygon_nodes[i].y > self.ymax and self.polygon_nodes[(i+1)%n].y <= self.ymax):
                #m=y2-y1/x2-x1
                m=float((self.polygon_nodes[(i+1)%n].y-self.polygon_nodes[i].y)/(self.polygon_nodes[(i+1)%n].x-self.polygon_nodes[i].x))
                m=round(m,2)
                #intersecting points: [y=ymax, x=(ymax-y)/m + x1]
                x_int=round(((self.ymax-self.polygon_nodes[i].y)/m)+self.polygon_nodes[i].x,2)
                y_int=self.ymax
                new_output_lst.append(vertex(x_int,y_int))

                #another point is the vertex-2
                x=self.polygon_nodes[(i+1)%n].x
                y=self.polygon_nodes[(i+1)%n].y
                new_output_lst.append(vertex(x,y))
                

            #if vertex 1 is inside and vertex 2 is outside, then save the intersecting point only
            if(self.polygon_nodes[i].y<=self.ymax and self.polygon_nodes[(i+1)%n].y>self.ymax):
                #m=y2-y1/x2-x1
                m=float((self.polygon_nodes[(i+1)%n].y-self.polygon_nodes[i].y)/(self.polygon_nodes[(i+1)%n].x-self.polygon_nodes[i].x))
                m=round(m,2)
                #intersecting points: [y=ymax, x=(ymax-y)/m + x1]
                x_int=round(((self.ymax-self.polygon_nodes[i].y)/m)+self.polygon_nodes[i].x,2)
                y_int=self.ymax
                new_output_lst.append(vertex(x_int,y_int))

        
        self.n=len(new_output_lst)
        self.polygon_nodes = []
        for i in range(self.n):
            self.polygon_nodes.append(new_output_lst[i])
        #self.remove_duplicate()
        
    def right(self):

        new_output_lst=[]
        n=self.n

        for i in range(self.n):
            '''
            we have used modulo for second vertex index so that when it reaches
            the end vertex, then it can be connected to the first vertex
            '''
            
            #if both vertices are outside, then do nothing
            if(self.polygon_nodes[i].x > self.xmax and self.polygon_nodes[(i+1)%n].x > self.xmax):
                continue

            #both vertices are inside, save the second vertex
            if(self.polygon_nodes[i].x <= self.xmax and self.polygon_nodes[(i+1)%n].x <= self.xmax):
                x=self.polygon_nodes[(i+1)%n].x
                y=self.polygon_nodes[(i+1)%n].y
                new_output_lst.append(vertex(x,y))

            #if vertex 1 is outside and vertex 2 is inside, save intersection and 2nd point
            if(self.polygon_nodes[i].x > self.xmax and self.polygon_nodes[(i+1)%n].x<= self.xmax):
                #m=y2-y1/x2-x1
                m=float((self.polygon_nodes[(i+1)%n].y-self.polygon_nodes[i].y)/(self.polygon_nodes[(i+1)%n].x-self.polygon_nodes[i].x))
                m=round(m,2)
                #intersecting points: [x=xmin, y=y1+m(xmax-x1)]
                x_int=self.xmax
                y_int=round(m*(x_int-self.polygon_nodes[i].x)+self.polygon_nodes[i].y,2)
                new_output_lst.append(vertex(x_int,y_int))

                #another point is the vertex-2
                x=self.polygon_nodes[(i+1)%n].x
                y=self.polygon_nodes[(i+1)%n].y
                new_output_lst.append(vertex(x,y))
                

            #if vertex 1 is inside and vertex 2 is outside, then save the intersecting point only
            if(self.polygon_nodes[i].x<=self.xmax and self.polygon_nodes[(i+1)%n].x>self.xmax):
                #m=y2-y1/x2-x1
                m=float((self.polygon_nodes[(i+1)%n].y-self.polygon_nodes[i].y)/(self.polygon_nodes[(i+1)%n].x-self.polygon_nodes[i].x))
                m=round(m,2)
                #intersecting points: [x=xmin, y=y1+m(xmax-x1)]
                x_int=self.xmax
                y_int=round(m*(x_int-self.polygon_nodes[i].x)+self.polygon_nodes[i].y,2)
                new_output_lst.append(vertex(x_int,y_int))
                

        self.n=len(new_output_lst)
        self.polygon_nodes=new_output_lst
        #self.remove_duplicate()

    def bottom(self):

        new_output_lst=[]
        n=self.n

        for i in range(n):

            #if both the vertices are outside the below edge
            #if(self.polygon_nodes[i].y<self.ymin and self.polygon_nodes[(i+1)%n].y<self.ymin):
             #   continue

            #both vertices are inside, save the second vertex
            if(self.polygon_nodes[i].y >= self.ymin and self.polygon_nodes[(i+1)%n].y >= self.ymin):
                x=self.polygon_nodes[(i+1)%n].x
                y=self.polygon_nodes[(i+1)%n].y
                new_output_lst.append(vertex(x,y))

            #if vertex 1 is outside and vertex 2 is inside, save intersection and 2nd point
            if(self.polygon_nodes[i].y < self.ymin and self.polygon_nodes[(i+1)%n].y >= self.ymin):

                #m=y2-y1/x2-x1
                m=float((self.polygon_nodes[(i+1)%n].y-self.polygon_nodes[i].y)/(self.polygon_nodes[(i+1)%n].x-self.polygon_nodes[i].x))
                m=round(m,2)
                
                #intersecting points: [y=ymax, x=(ymax-y)/m + x1]
                x_int=round(((self.ymin-self.polygon_nodes[i].y)/m)+self.polygon_nodes[i].x,2)
                y_int=self.ymin
                new_output_lst.append(vertex(x_int,y_int))

                #another point is the vertex-2
                x=self.polygon_nodes[(i+1)%n].x
                y=self.polygon_nodes[(i+1)%n].y
                new_output_lst.append(vertex(x,y))
                

            #if vertex 1 is inside and vertex 2 is outside, then save the intersecting point only
            if(self.polygon_nodes[i].y>= self.ymin and self.polygon_nodes[(i+1)%n].y< self.ymin):
                #m=y2-y1/x2-x1
                m=float((self.polygon_nodes[(i+1)%n].y-self.polygon_nodes[i].y)/(self.polygon_nodes[(i+1)%n].x-self.polygon_nodes[i].x))
                m=round(m,2)
                
                #intersecting points: [y=ymax, x=(ymax-y)/m + x1]
                x_int=round(((self.ymin-self.polygon_nodes[i].y)/m)+self.polygon_nodes[i].x,2)
                y_int=self.ymin
                new_output_lst.append(vertex(x_int,y_int))

        self.n=len(new_output_lst)
        self.polygon_nodes=new_output_lst
        #self.remove_duplicate()


    def remove_duplicate(self):

        for i in range(len(self.polygon_nodes)):
            v=self.polygon_nodes[i]
            if(i==len(self.polygon_nodes)-1):
                break
            
            for j in range(i+1,len(self.polygon_nodes)):
                w=self.polygon_nodes[j]    
                if(v.x==w.x and v.y==w.y):
                    del self.polygon_nodes[j]

        
        
    def __str__(self):

        lst=[]
        for i in range(len(self.polygon_nodes)):
            v=self.polygon_nodes[i]
            print('NODE-'+str(i+1)+': ','(',v.x,',',v.y,')')
            lst.append([v.x,v.y])

        return 'UPDATED NODES OF NEW CLIPPED POLYGON : '+str(lst)

def main():

    s=sutherland_clip()
    s.input()
    
    s.left()
    print('LEFT EDGE :-------------')
    print(s,'\n')

    s.top()
    print('TOP EDGE :--------------')
    print(s,'\n')

    s.right()
    print('RIGHT EDGE :-------------')
    print(s,'\n')
    
    s.bottom()
    print('BOTTOM EDGE :---------------')
    print(s,'\n')

if __name__=='__main__':

    main()
