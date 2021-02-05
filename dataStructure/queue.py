class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    @property
    def isEmpty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

    @property
    def size(self):
        return len(self.items)

    def update(self, items):
        self.items = list(items)[::-1] + self.items
