# 使用双端队列建立一个回文检测器
from dataStructure.deque import Deque


def palChecker(astring):
    charDeque = Deque()
    for char in astring:
        charDeque.addrear(char)

    stillEqual = True
    while stillEqual and charDeque.size > 1:
        front = charDeque.removefront()
        end = charDeque.removerear()
        if front != end:
            stillEqual = False
    return stillEqual
