class Deque(object):
    def __init__(self):
        self.items = []

    def addfront(self, item):
        self.items.insert(0, item)

    def addrear(self, item):
        self.items.append(item)

    def removefront(self):
        return self.pop(0)

    def removerear(self):
        return self.pop()

    @property
    def size(self):
        return len(self.items)
