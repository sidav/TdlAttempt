from SidavRandom import * #Can be deleted if the following wrapper will be handled
from ConsoleWrapper import  *


def random(min, max): #IT'S JUST A WRAPPER. Min, max inclusive!
    return rand(max-min+1)+min


class treeNode:
    def __init__(self, parent=None, cont=None):
        self.parent = parent
        self.left = None
        self.right = None
        self.cont = cont

    def getLevel(self, lvl, nodelist=None): #should be called from the root only
        if nodelist == None:
            nodelist = []
        if lvl == 0:
            nodelist.append(self)
        else:
            if self.left is not None:
                self.left.getLevel(lvl-1, nodelist)
            if self.right is not None:
                self.right.getLevel(lvl-1, nodelist)
        return nodelist

    def getLeafs(self, leafs=None):
        if leafs == None:
            leafs = []
        if self.left is None and self.right is None:
            leafs.append(self)
        if self.left is not None:
            self.left.getLeafs(leafs)
        if self.right is not None:
            self.right.getLeafs(leafs)
        return leafs

    def split(self): #BSP splitting
        factor = random(MIN_SPLIT_FACTOR, MAX_SPLIT_FACTOR)
        selfx = self.cont.x
        selfy = self.cont.y
        selfw = self.cont.w
        selfh = self.cont.h
        lefthorizh = selfh*factor//100
        righthorizh = selfh - lefthorizh
        leftvertw = selfw*factor//100
        rightvertw = selfw - leftvertw
        horiz = random(0, 1) #0 is horizontal splitting, 1 is vertical
        if horiz == 0:
            leftc = Container(selfx, selfy, selfw, lefthorizh)
            rightc = Container(selfx, lefthorizh, selfw, righthorizh)
            self.left = treeNode(self, leftc)
            self.right = treeNode(self, rightc)
        else:
            leftc = Container(selfx, selfy, leftvertw, selfh)
            rightc = Container(leftvertw, selfy, rightvertw, selfh)
            self.left = treeNode(self, leftc)
            self.right = treeNode(self, rightc)


class Container:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def draw(self):
        drawRect(self.x,self.y,self.w,self.h)

    def output(self): #for debug purposes
        print("x = %i, y = %i, w = %i, h = %i" % (self.x,self.y,self.w,self.h))


def splitNTimes(N):
    for _ in range(N):
        leafs = BSPRoot.getLeafs()
        for l in leafs:
            l.split()

def doShit(): #delete this somewhen
    global BSPRoot
    con = Container(0,0,80,25)
    BSPRoot = treeNode(cont = con)
    splitNTimes(3)
    leafs = BSPRoot.getLeafs()
    for i in leafs:
        i.cont.output()
        i.cont.draw()


MAP_WIDTH = 80
MAP_HEIGHT = 25
MIN_SPLIT_FACTOR = 40 #IT will be divided by 100 somewhen
MAX_SPLIT_FACTOR = 60 #It too
MIN_ROOM_SIZE = 2
BSPRoot = None#treeNode(cont=Container(0,0,MAP_WIDTH, MAP_HEIGHT))

# FLOOR = 0
# WALL = 1
# DOOR = 2


