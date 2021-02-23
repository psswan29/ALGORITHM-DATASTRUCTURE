# 汉诺塔问题
# 1.借助终点柱子，将高度为height-1的一叠盘子移到中间柱子；
# 2.将最后一个盘子移到终点柱子；
# 3.借助起点，将高度为height-1的一叠盘子从中间柱子移到终点柱子


class Stack():
    def __init__(self, height=0):
        self.items = []
        self.height = height

    def add(self, item):
        self.items.append(item)

    def get_item(self, index):
        return self.items.pop(index)

    def pop(self):
        return self.items.pop()


def moveTower(height, fromPole, toPole, withPole, stacking):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole, stacking)
        moveDisk(fromPole, toPole, stacking)
        moveTower(height - 1, withPole, toPole, fromPole, stacking)


def moveDisk(fromPole, toPole, stacking):
    print(f'moving from {fromPole} to {toPole}')
    stacking.append(f'moving from {fromPole} to {toPole}')


fromPole = Stack()
toPole = Stack()
withPole = Stack()


def searchForm(maze, startRow, startColumn):
    maze.updatePosition(startRow, startColumn)


# 小乌龟探索迷宫
from turtle import *


class Maze(object):
    # 读入一个代表迷宫的数据文件，初始化迷宫的内部表示，
    # 并且找到小乌龟的其实位置
    def __init__(self, mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        mazeFile = open(mazeFileName, 'r')
        rowsInMaze = 0
        for line in mazeFileName:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)

        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.xTranslate = -columnsInMaze / 2
        self.yTranslate = rowsInMaze / 2
        self.t = Turtle(shape='turtle')
        self.t.getscreen().setup(width=600, height=600)
        self.t.getscreen().setworldcoordinates(-(columnsInMaze - 1) / 2 - 0.5,
                                               -(rowsInMaze - 1) / 2 - 0.5,
                                               (columnsInMaze - 1) / 2 + 0.5,
                                               (rowsInMaze - 1) / 2 + 0.5
                                               )
