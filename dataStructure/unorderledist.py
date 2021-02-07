class Node(object):
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, next):
        self.next = next


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        # 若将下面两行颠倒则会导致已有节点丢失
        temp.setNext(self.head)
        self.head = temp

    @property
    def length(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.getNext()
        return count

    def search(self, item):
        found = False
        temp = self.head
        while temp.getData() != item:
            temp = temp.getNext()
            if not temp:
                return found
        found = True
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
                # 这里要小心若是第一个就找到了item
                if previous:
                    previous.setNext(current.getNext())
                else:
                    self.head = current.getNext()
            else:
                previous = current
                current = current.getNext()

    def insert(self, index, item):
        new_node = Node(item)
        current_ix = 0
        current = self.head
        previous = None

        while current_ix < index:
            current_ix += 1
            previous = current
            current = current.getNext()
        if previous:
            previous.setNext(new_node)
        else:
            self.head = new_node
        new_node.setNext(current)

    #   返回索引，若没有找到则返回-1
    def index(self, item):
        current = self.head
        i = 0
        found = False
        while current:
            if current.getData() == item:
                found = True
                break
            current = current.getNext()
            i += 1
        if not found:
            i = -1
        return i
