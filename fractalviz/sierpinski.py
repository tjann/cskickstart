'''This program draws a Sierpinski triangle
'''

import sys
from graphics import *

class Sierpinski:
    def __init__(self, left, top, width, depth):
        self.left = left
        self.top = top
        self.width = width
        self.depth = depth

    def drawTriangle(self, window, left, top, legLength):
        line = Line(Point(left, top), Point(left + legLength, top))
        line.draw(window)
        line = Line(Point(left + legLength, top), Point(left, top + legLength))
        line.draw(window)
        line = Line(Point(left, top + legLength), Point(left, top))
        line.draw(window)

    def drawSection(self, window, x, y, legLength, depth):
        if depth > 0:
            # Draw the big triangle.
            self.drawTriangle(window, x, y, legLength)

            # Draw the three little sections.
            halfLeg = legLength / 2
            self.drawSection(window, x + halfLeg, y - halfLeg, halfLeg, depth - 1)
            self.drawSection(window, x - halfLeg, y + halfLeg, halfLeg, depth - 1)
            self.drawSection(window, x + halfLeg, y + halfLeg, halfLeg, depth - 1)


    def draw(self, window):
        self.drawSection(window, self.left, self.top, self.width, self.depth)

if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print('Usage: %s numberOfLevels' % sys.argv[0])
        exit()

    window = GraphWin('Sierpinski Triangle Demo', 800, 800)
    window.setBackground(color_rgb(255, 255, 255))

    numberOfLevels = int(sys.argv[1])
    sierpinskiTriangle = Sierpinski(400, 400, 300, numberOfLevels)
    sierpinskiTriangle.draw(window)
    window.getMouse()
    window.close()
