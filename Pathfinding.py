import numpy
import math

  #Here I'll try to implement the A* pathfinding.
  #Yes, it is a horrible shit.

######################################
class Node:
    x = y = g = 0
    passable = True
    neighbours = []

    def __init__(self, x, y, parent=None, g=0, h=0):
        self.x = x
        self.y = y
        self.parent = parent
        self.g = g
        self.h = h

    def set_g(self, g_):
        self.g = g_

    def is_equal(self, anothercell):
        return (self.x == anothercell.x and self.y == anothercell.y)


#######################################

class Pathfinder:

    STRAIGHT_COST = 10
    DIAGONAL_COST = 14
    nodemap = []
    openlist = [] #list of cells which we have to check
    closedlist = [] #list of checked cells

    def calc_H(self, fromx, fromy, tox, toy):
        return 10*abs(tox-fromx + toy-fromy)

    def __init__(self, inpboolmap):
        self.boolmap = inpboolmap
        pass
