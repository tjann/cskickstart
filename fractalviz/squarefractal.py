''' This program draws a T-square fractal.
    Call this program like:
    python squarefractal.py 9
'''

import sys
from graphics import *

class SquareFractal:
    def __init__(self, centerX, centerY, totalLength, depth):
        self.centerX = centerX # center of square
        self.centerY = centerY
        self.totalLength = totalLength # total length of art space
        self.depth = depth # max recursion depth

    def drawSquare(self, win, ctrX, ctrY, l):
        p1 = Point(ctrX - l/4, ctrY - l/4) # lower left corner
        p2 = Point(ctrX + l/4, ctrY + l/4) # upper right corner

        rect = Rectangle(p1,p2) # construct the rectangle
        #rect.setFill(color_rgb(0,0,0)) # try commenting out to see what happens (recursion might be more clear without filling in the squares)
        rect.draw(win) # draw the rectangle in the window
    
    def drawSection(self, win, ctrX, ctrY, l, depth):
        # Draw the big square
        if depth > 0:
            self.drawSquare(win, ctrX, ctrY, l)
            # Recursive calls: draw the smaller squares
            self.drawSection(win, ctrX - l/4, ctrY - l/4, l/2, depth - 1) # lower left
            self.drawSection(win, ctrX - l/4, ctrY + l/4, l/2, depth - 1) # upper left
            self.drawSection(win, ctrX + l/4, ctrY - l/4, l/2, depth - 1) # lower right
            self.drawSection(win, ctrX + l/4, ctrY + l/4, l/2, depth - 1) # upper right
            
    def draw(self, window):
        self.drawSection(window, self.centerX, self.centerY, self.totalLength, self.depth) # LET THE FUN BEGIN

if __name__ == '__main__':
    # This just makes sure the arguments are valid
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print('Usage: %s numberOfLevels' % sys.argv[0])
        exit(1)
    win = GraphWin("My Swuare Fractal", 800, 800) # window init and size
    win.setBackground(color_rgb(255, 255, 255)) # sets white background

    numberOfLevels = int(sys.argv[1]) # max recursion depth
    squareFractal = SquareFractal(400, 400, 800, numberOfLevels) # init fractal object
    squareFractal.draw(win) # LET THE FUN BEGIN
    win.getMouse() # pause until click
    win.close()
