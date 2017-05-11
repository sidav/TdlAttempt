from SidavRandom import * #Can be deleted if the following wrapper will be handled
from ConsoleWrapper import drawCharArray, setForegroundColor, putChar


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

    def addToMap(self, arr):
        x0 = self.x-1
        y0 = self.y-1
        h = self.h+1
        w = self.w+1
        for i in range(x0, x0 + w):
            arr[i][y0] = "#"
            arr[i][y0+h-1] = "#"
        for j in range(y0, y0 + h):
            arr[x0][j] = "#"
            arr[x0+w-1][j] = "#"

    # def draw(self): #for debug purposes
    #     drawRect(self.x-1,self.y-1,self.w+1,self.h+1)

    def output(self): #for debug purposes
        print("x = %i, y = %i, w = %i, h = %i, splitting was %s" % (self.x,self.y,self.w,self.h, self.vh))
#############################################################################################################
#############################################################################################################
def splitNTimes(root, N):
    for _ in range(N):
        leafs = root.getLeafs()
        for l in leafs:
            l.split()

def placeConnections(root, arr):
    # the following loop will draw the connections between the nodes with the same parent.
    # It creates the smth like doorways or even removes some walls.
    # I'm glad of the result. Really.
    traverseEnded = False
    curlvl = 0
    while not traverseEnded:
        a = root.getLevel(curlvl)
        if len(a) is 0:
            traverseEnded = True
        for i in a:
            if i.left is not None and i.right is not None:
                fx = i.left.cont.x + i.left.cont.w // 2
                fy = i.left.cont.y + i.left.cont.h // 2
                tx = i.right.cont.x + i.right.cont.w // 2
                ty = i.right.cont.y + i.right.cont.h // 2
                if fx == tx:
                    for k in range(fy, ty + 1):
                        arr[fx][k] = " "
                elif fy == ty:
                    for k in range(fx, tx + 1):
                        arr[k][fy] = " "
        curlvl += 1

def placeDoors(arr):
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[0])-1):
            #horizontal doors:
            if arr[i][j] == " " and arr[i][j-1] == "#" and arr[i][j+1] == "#" and arr[i-1][j] == " " and arr[i+1][j] == " ":
                arr[i][j] = "+"
                #DELETE THE FOLLOWING:
                setForegroundColor(255,0,0)
                putChar("+", i, j)
            #vertical doors:
            elif arr[i][j] == " " and arr[i-1][j] == "#" and arr[i+1][j] == "#" and arr[i][j-1] == " " and arr[i][j+1] == " ":
                arr[i][j] = "+"
                # DELETE THE FOLLOWING:
                setForegroundColor(255, 0, 0)
                putChar("+", i, j)



def doShit(): #delete this somewhen
    outp = [[" "] * (MAP_HEIGHT+1) for _ in range(MAP_WIDTH+1)]
    con = Container(1,1,79,24)
    BSPRoot = treeNode(cont = con)
    splitNTimes(BSPRoot, 6)
    leafs = BSPRoot.getLeafs()
    for i in leafs:#leafs:
        # i.cont.output()
        # i.cont.draw()
        i.cont.addToMap(outp)
    placeConnections(BSPRoot, outp)
    # draw the char array (it is just for debug)
    setForegroundColor(255, 255, 255)
    drawCharArray(outp)
    
    placeDoors(outp)



MAP_WIDTH = 80
MAP_HEIGHT = 25
MIN_SPLIT_FACTOR = 25 #IT will be divided by 100 somewhen
MAX_SPLIT_FACTOR = 75 #It too
MIN_ROOM_SIZE = 3

# FLOOR = 0
# WALL = 1
# DOOR = 2


