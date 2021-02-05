# 传土豆模拟程序
import random

from dataStructure.queue import Queue


# 使用队列模拟一个环，假设握着土豆的孩子位于队列的头部。在模拟传土豆的过程中，
# 程序将这个孩子的名字移除队列，然后立刻将其插入队列的尾部。随后，这个孩子会一直等待，
# 直到再次到达队列的头部。在出列和入列num次，此时位于队列头部的孩子出局，新一轮游戏开始，
# 如此反复直至队列中只剩下了一个孩子


def hot_potato(namelist, num=None):
    if not num:
        num = random.randint(1, 11)
    nameQueue = Queue()
    for name in namelist:
        nameQueue.enqueue(name)

    while nameQueue.size > 1:
        # 转圈，每隔几个人
        for i in range(num):
            nameQueue.enqueue(nameQueue.dequeue())
        nameQueue.dequeue()
    return nameQueue.dequeue()


class Student(object):
    students = set()
    available_print_num = 2

    def __init__(self):
        self.studentID = random.randint(1000, 9999)
        while self.studentID in self.students:
            self.studentID = random.randint(1000, 9999)
        self.students.add(self.studentID)

        self.taskNum = 0

    def gen_task(self, task_queue, pages):
        if self.taskNum == self.available_print_num:
            print('已达到个人最大打印限额！！！')
            return
        self.taskNum += 1
        new_task = Task(pages, self.studentID)
        return new_task

    @classmethod
    def get_student_num(cls):
        return len(cls.students)


# printer 类会检查当前有待完成的任务，如果有就处于工作状态，
# 并且工作所需的时间可以通过打印来计算。其方法会初始化打印速度，即每分钟多少页。
# tick方法会减量计时，并且在执行完任务后打印机设置为空置状态

class Printer(object):
    def __init__(self, ppm):
        self.currentTask = None
        self.pagerate = ppm
        self.timeremaining = 0

    def tick(self):
        if self.currentTask:
            self.timeremaining = self.timeremaining - 1
            if self.timeremaining <= 0:
                self.currentTask = None

    @property
    def busy(self):
        if self.currentTask:
            return True
        else:
            return False

    def startNext(self, nexttast):
        self.currentTask = nexttast
        self.timeremaining = nexttast.getPages() * 60 / self.pagerate


class Task(object):
    def __init__(self, pages, contributor: Student.studentID, timestamp):
        self.pages = pages
        self.contributor = contributor
        self.timestamp = timestamp

    def getPages(self):
        return self.pages

    def getTimestamp(self):
        return self.timestamp

    def getContributor(self):
        return self.contributor

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


class printQueue(object):
    def __init__(self):
        pass


#   打印任务模拟程序,
def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy) and (not printQueue.isEmpty):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print('Average wait %6.2f secs %3d tasks remaining.' % (averageWait, printQueue.size))


def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False
