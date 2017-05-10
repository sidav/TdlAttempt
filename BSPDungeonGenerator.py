from SidavRandom import * #Can be deleted if the following wrapper will be handled
from ConsoleWrapper import *


def random(min, max): #IT'S JUST A WRAPPER. Min, max inclusive!
    return rand(max-min+1)+min


class treeNode:
    def __init__(self, parent=None, cont=None):
        self.parent = parent
        self.left = None
        self.right = None
        self.cont = cont

    def getLevel(self, lvl, nodelist=None): #should be called from the root node only
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
        selfx = self.cont.x
        selfy = self.cont.y
        selfw = self.cont.w
        selfh = self.cont.h
        horiz = random(0, 1)  # 1 is horizontal splitting, 0 is vertical
        for _ in range(5): #5 is just a number of tries
            horizOK = True
            vertOK = True
            factor = random(MIN_SPLIT_FACTOR, MAX_SPLIT_FACTOR)
            lefthorizh = selfh*factor//100
            righthorizh = selfh - lefthorizh
            leftvertw = selfw*factor//100
            rightvertw = selfw - leftvertw
            if (lefthorizh < MIN_ROOM_SIZE or righthorizh < MIN_ROOM_SIZE):
                horiz = 0
                horizOK = False
            if (leftvertw < MIN_ROOM_SIZE or rightvertw < MIN_ROOM_SIZE):
                vertOK = False
                continue
        if not (horizOK and vertOK):
            return
        if horiz == 1: #horizontal split
            leftc = Container(selfx, selfy, selfw, lefthorizh, "LHORIZONTAL")
            rightc = Container(selfx, selfy+lefthorizh, selfw, righthorizh, "RHORIZONTAL")
            self.left = treeNode(self, leftc)
            self.right = treeNode(self, rightc)
        else: #vertical split
            leftc = Container(selfx, selfy, leftvertw, selfh, "LVERTICAL")
            rightc = Container(selfx+leftvertw, selfy, rightvertw, selfh, "RVERTICAL")
            self.left = treeNode(self, leftc)
            self.right = treeNode(self, rightc)


class Container:
    def __init__(self, x, y, w, h, vh = "UNDEF"):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vh = vh

    def draw(self): #for debug purposes
        drawRect(self.x-1,self.y-1,self.w+1,self.h+1)

    def output(self): #for debug purposes
        print("x = %i, y = %i, w = %i, h = %i, splitting was %s" % (self.x,self.y,self.w,self.h, self.vh))


def splitNTimes(N):
    for _ in range(N):
        leafs = BSPRoot.getLeafs()
        for l in leafs:
            l.split()

def doShit(): #delete this somewhen
    global BSPRoot
    con = Container(1,1,70,24)
    BSPRoot = treeNode(cont = con)
    splitNTimes(6)
    leafs = BSPRoot.getLeafs()
    for i in BSPRoot.getLevel(3):#leafs:
        setForegroundColor(255,0,0)
        # i.cont.output()
        i.cont.draw()
    for i in BSPRoot.getLeafs():#leafs:
        setForegroundColor(255, 255, 255)
        # i.cont.output()
        i.cont.draw()


MAP_WIDTH = 80
MAP_HEIGHT = 25
MIN_SPLIT_FACTOR = 20 #IT will be divided by 100 somewhen
MAX_SPLIT_FACTOR = 80 #It too
MIN_ROOM_SIZE = 2
BSPRoot = None#treeNode(cont=Container(0,0,MAP_WIDTH, MAP_HEIGHT))

# FLOOR = 0
# WALL = 1
# DOOR = 2


