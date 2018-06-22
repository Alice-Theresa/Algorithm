from Queue import Queue
from Debug import inputLog
from Debug import DebugSetting

class Graph:

    Debug = DebugSetting()['Graph']

    def __init__(self):
        self.vertices = []
        self.lines = {}
        self.colors = {}

    @inputLog(Debug)
    def addVertex(self, v):
        self.vertices.append(v)
        self.lines[v] = []

    @inputLog(Debug)
    def addEdge(self, v, w):
        self.lines[v].append(w)
        self.lines[w].append(v)

    def showGraph(self):
        for i in self.vertices:
            s = i + ' -> '
            for j in self.lines[i]:
                s = s + j + ' '
            print(s)

    def initializeColor(self):
        for i in self.vertices:
            self.colors[i] = 'white'

    def bfs(self, v):
        print('--- bfs ---')

        self.initializeColor()
        queue = Queue()
        queue.enqueue(v)
        result = []

        while not queue.isEmpty():
            u = queue.dequeue()
            neighbors = self.lines[u]
            self.colors[u] = 'gray'
            for i in neighbors:
                if self.colors[i] == 'white':
                    self.colors[i] = 'gray'
                    queue.enqueue(i)
            self.colors[u] = 'black'
            result.append(u)
        print(result)

    def dfs(self):
        print('--- dfs ---')
        self.initializeColor()
        for i in self.vertices:
            if self.colors[i] == 'white':
                self.__dfs(i)

    def __dfs(self, v):
        self.colors[v] = 'gray'
        print(v)
        neighbors = self.lines[v]
        for i in neighbors:
            if self.colors[i] == 'white':
                self.__dfs(i)
        self.colors[i] = 'black'

if __name__ == "__main__":
    g = Graph()
    g.addVertex('a')
    g.addVertex('b')
    g.addVertex('c')
    g.addVertex('d')
    g.addVertex('e')
    g.addVertex('f')
    g.addEdge('a', 'b')
    g.addEdge('a', 'c')
    g.addEdge('a', 'd')
    g.addEdge('b', 'e')
    g.addEdge('c', 'f')
    g.addEdge('e', 'f')
    g.showGraph()

    g.bfs('a')
    g.dfs()
