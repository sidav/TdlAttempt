import numpy

  #Here I'll try to implement the A* pathfinding.

class pathfinder:

    boolMap = numpy.zeros((80, 25))  #[[[False for x in range(80)] for y in range(25)]]

    def __init__(self, inpBoolMap):
        global boolMap
        boolMap = inpBoolMap
