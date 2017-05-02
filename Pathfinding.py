import numpy
import math

  #Here I'll try to implement the A* pathfinding.
  #Yes, it is a horrible shit.

######################################
class Node:
    #x = y = g = 0
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
    openlist = [] #list of cells which we have to check
    closedlist = [] #list of checked cells

    def calc_H(self, fromx, fromy, tox, toy):
        return 10*abs(tox-fromx + toy-fromy)

    def nodeExists(self, x, y):
        if 0 <= x < len(self.nodemap) and 0 <= y < len(self.nodemap[0]):
            return True
        return False

    def boolmapToNodemap(self):
        #firstly, let's make nodes array from simpru bool array
        for x in range(len(self.boolmap)):
            for y in range(len(self.boolmap[0])):
                isPassable = self.boolmap[x][y]
                self.nodemap[x][y] = Node(x, y, None, 0, 0)
                self.nodemap[x][y].passable = isPassable
        #Ok, it's hopefully done. Let's give the neighbours to the every fucking node out there:
        #Notice that we will add only the passable fucking neighbours, not any fucking neighbours.
        for x in range(len(self.nodemap)):
            for y in range(len(self.nodemap[0])):
                curnode = self.nodemap[x][y]
                for i in (-1, 0, 1):
                    for j in (-1, 0, 1):
                        if self.nodeExists(x+i, y+j) and (i != 0 or j != 0):
                            if self.nodemap[x+i][y+j].passable:
                                curnode.neighbours.append(self.nodemap[x+i][y+j])
        #Heeeere we are. I REALLY hope that this shit will fucking work at all.


    def __init__(self, inpboolmap):
        x = len(inpboolmap)
        y = len(inpboolmap[0])
        self.boolmap = inpboolmap #if true, then the given cell is passabru!
        self.nodemap = A = [[0] * y for _ in range(x)] #да, эта дрянь создаёт список списков, ширина которого x, высота у
        pass

#АЛГОРИТМ А*: 
# 1) Добавляем стартовую клетку в открытый список.
#
# 2) Повторяем следующее:
#
# a) Ищем в открытом списке клетку с наименьшей стоимостью F. Делаем ее текущей клеткой.
#
# b) Помещаем ее в закрытый список. (И удаляем с открытого)
#
# c) Для каждой из соседних 8-ми клеток ...
#
# Если клетка непроходимая или она находится в закрытом списке, игнорируем ее. В противном случае делаем следующее.
#
# Если клетка еще не в открытом списке, то добавляем ее туда. Делаем текущую клетку родительской для это клетки. Расчитываем стоимости F, G и H клетки.
#
# Если клетка уже в открытом списке, то проверяем, не дешевле ли будет путь через эту клетку. Для сравнения используем стоимость G. Более низкая стоимость G указывает на то, что путь будет дешевле. Эсли это так, то меняем родителя клетки на текущую клетку и пересчитываем для нее стоимости G и F. Если вы сортируете открытый список по стоимости F, то вам надо отсортировать свесь список в соответствии с изменениями.
#
# d) Останавливаемся если:
#
# Добавили целевую клетку в открытый список, в этом случае путь найден.
# Или открытый список пуст и мы не дошли до целевой клетки. В этом случае путь отсутствует.
# 3) Сохраняем путь. Двигаясь назад от целевой точки, проходя от каждой точки к ее родителю до тех пор, пока не дойдем до стартовой точки. Это и будет наш путь.