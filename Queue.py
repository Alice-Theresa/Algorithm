from Debug import inputLog
from Debug import outputLog
from Debug import DebugSetting

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class Queue:

    Debug = DebugSetting()['Queue']

    def __init__(self):
        super().__init__()
        self.front = None
        self.end = None

    @inputLog(Debug)
    def enqueue(self, data):
        node = Node(data)
        if self.front == None:
            self.front = node
            self.end = node
        else:
            self.end.next = node
            self.end = node

    @outputLog(Debug)
    def dequeue(self):
        if self.front != None:
            temp = self.front.data
            self.front = self.front.next
            return temp
        else:
            return None

    @outputLog(Debug)
    def isEmpty(self):
        return self.front == None

    @outputLog(Debug)
    def totalCount(self):
        count = 0
        temp = self.front
        while temp != None:
            count += 1
            temp = temp.next
        return count

    def showQueue(self):
        temp = self.front
        q = 'Head - '
        while temp != None:
            q = q + str(temp.data) + ' - '
            temp = temp.next
        q = q + 'Tail'
        print(q)

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.showQueue()
    q.dequeue()
    q.dequeue()
    q.showQueue()
    q.isEmpty()
    q.totalCount()
    q.showQueue()
    q.enqueue(5)
    q.enqueue(6)
    q.showQueue()
    q.dequeue()
    q.dequeue()
    q.showQueue()
