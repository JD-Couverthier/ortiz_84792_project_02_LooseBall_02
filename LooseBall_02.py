from graphics import *


def figure_left(figure):
    figure.move(-15, 0)

def figure_right(figure):
    figure.move(15, 0)

def figure_up(figure):
    figure.move(0, -15)

def figure_down(figure):
    figure.move(0, 15)


def window():
    #Window
     win = GraphWin("Loose Ball", 600, 600)
     win.setBackground("green")
     return win

def drawfigure(win):
     figure = Rectangle(Point(100, 100), Point(100, 100))
     figure.setOutline("blue")
     figure.setFill("blue")
     figure.draw(win)
     figure.move(9, 9)
     figure.setWidth(40)