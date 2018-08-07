from graphics import *
import sys


class SquareFractal:
    def __init__(self, centerX, centerY, totalLength, depth):
        self.centerX = centerX
        self.centerY = centerY
        self.totalLength = totalLength
        self.depth = depth

    def drawSquare(self, win, ctrX, ctrY, l):
        p1 = Point(ctrX - l/4, ctrY - l/4)
        p2 = Point(ctrX + l/4, ctrY + l/4)

        rect = Rectangle(p1,p2)
        rect.setFill(color_rgb(0,0,0))
        rect.draw(win)
    
    def drawSection(self, win, ctrX, ctrY, l, depth):
        # Draw the big square
        print(ctrX, ctrY, l)
        if depth > 0:
            self.drawSquare(win, ctrX, ctrY, l)
            # Draw the smaller squares
            
            self.drawSection(win, ctrX - l/4, ctrY - l/4, l/2, depth - 1)
            #self.drawSection(win, ctrX - l/4, ctrY, l/4, depth - 1)
            self.drawSection(win, ctrX - l/4, ctrY + l/4, l/2, depth - 1)
            #self.drawSection(win, ctrX, ctrY - l/4, l/4, depth - 1)
            #self.drawSection(win, ctrX, ctrY + l/4, l/4, depth - 1)
            self.drawSection(win, ctrX + l/4, ctrY - l/4, l/2, depth - 1)
            #self.drawSection(win, ctrX + l/4, ctrY, l/4, depth - 1)
            self.drawSection(win, ctrX + l/4, ctrY + l/4, l/2, depth - 1)
            
    def draw(self, window):
        self.drawSection(window, self.centerX, self.centerY, self.totalLength, self.depth)

if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print('Usage: %s numberOfLevels' % sys.argv[0])
        exit(1)
    win = GraphWin("My Swuare Fractal", 800, 800)
    win.setBackground(color_rgb(255, 255, 255))

    numberOfLevels = int(sys.argv[1])
    squareFractal = SquareFractal(400, 400, 800, numberOfLevels)
    squareFractal.draw(win)
    win.getMouse()
    win.close()
    quit(0)
    def squares(ctrPoint, l):
        squares(Point(ctrPoint.x - 1/3, ctrPoint.y - 1/3))
        squares(Point(ctrPoint.x - 1/3, ctrPoint.y))
        squares(Point(ctrPoint.x - 1/3, ctrPoint.y + 1/3))
        squares(Point(ctrPoint.x, ctrPoint.y - 1/3))
        squares(Point(ctrPoint.x, ctrPoint.y + 1/3))
        squares(Point(ctrPoint.x + 1/3, ctrPoint.y - 1/3))
        squares(Point(ctrPoint.x + 1/3, ctrPoint.y))
        squares(Point(ctrPoint.x + 1/3, ctrPoint.y + 1/3))
        
        p1 = Point(ctrPoint.x - l/2, ctrPoint.y - l/2)
        p2 = Point(ctrPoint.x + l/2, ctrPoint.y + l/2)

        rect = Rectangle(p1,p2)
        rect.draw(win)
            
