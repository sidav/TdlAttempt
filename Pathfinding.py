import numpy
import math

  #Here I'll try to implement the A* pathfinding.


class Pathfinder:
    ######################################
    class Cell:
        x = y = g = 0
        def __init__(self, xcor, ycor, g_):
            global x, y, g
            x = xcor
            y = ycor
            g = g_
    #######################################

    STRAIGHT_COST = 10
    DIAGONAL_COST = 14
    boolMap = []
    openlist = [] #list of cells which we have to check
    closedlist = [] #list of checked cells

    def pathfindStart(self, fromx, fromy, tox, toy):
        global openlist, closedlist
        startnode = self.Cell(fromx, fromy, 0)
        openlist.append(startnode)
        closedlist.append(startnode)
        self.checkNeighbours()
        openlist.remove(startnode)


    def calc_H(self, fromx, fromy, tox, toy):
        return 10*abs(tox-fromx + toy-fromy)

    def checkNeighbours(self, curcell):
        x = curcell.x
        y = curcell.y
        pass


    def __init__(self, inpBoolMap):
        global boolMap
        pass
