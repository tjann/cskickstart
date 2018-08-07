from graphics import * 

def main(start, minr=1):

    print('You specified to make circles within a ' + str(start) + ' radius, starting with ' + str(minr))
    win = GraphWin("My Fractal", 1000, 1000)
    def circles(radius):
        if radius == minr:
            c = Circle(Point(500,500), radius)
            c.draw(win)
            print('Circle with radius', radius)
            time.sleep(1)
        else:
            circles(radius-20)
            c = Circle(Point(500,500), radius)
            c.draw(win)
            print('Circle with radius', radius)
            time.sleep(1)
    circles(start)
    #p1 = Point(0,0)
    #p2 = Point(800,800)

    #rect = Rectangle(p1,p2)
    #rect.draw(win)
    win.getMouse()
    win.close()
main(300, 100)
