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
