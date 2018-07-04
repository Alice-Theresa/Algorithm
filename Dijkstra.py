from Queue import Queue
from Debug import inputLog
from Debug import DebugSetting

# 只适用于有向无环图
class Dijkstra:

    Debug = DebugSetting()['Dijkstra']

    def __init__(self):
        self.graph = {}
        self.cost = {}
        self.father = {}
        self.start = None
        self.fin = None
        self.processed = []

    @inputLog(Debug)
    def addEdge(self, v, w=None, length=0):
        if self.graph == {}:
            self.start = v
        if not v in self.graph:
            self.graph[v] = {}
        if w is None:
            self.fin = v
        else:
            self.graph[v][w] = length
            self.cost[w] = float('inf')
            self.father[w] = None

    def buildCost(self):
        for node in self.graph.keys():
            if node == self.start:
                for key in self.graph[node].keys():
                    self.cost[key] = self.graph[node][key]

    def buildFather(self):
        for node in self.graph.keys():
            if node == self.start:
                for key in self.graph[node].keys():
                    self.father[key] = node

    def findLowestCostNode(self):
        lowsetCosts = float('inf')
        lowsetCostsNode = None
        for key in self.cost.keys():
            cost = self.cost[key]
            if cost < lowsetCosts and key not in self.processed:
                lowsetCosts = cost
                lowsetCostsNode = key
        return lowsetCostsNode

    def calculate(self):
        self.buildCost()
        self.buildFather()
        node = self.findLowestCostNode()
        while node is not None:
            cost = self.cost[node]
            neighbors = self.graph[node]
            for n in neighbors.keys():
                newCost = cost + neighbors[n]
                if self.cost[n] > newCost:
                    self.cost[n] = newCost
                    self.father[n] = node
            self.processed.append(node)
            node = self.findLowestCostNode()


if __name__ == '__main__':
    g = Dijkstra()
    g.addEdge('a', 'b', 6)
    g.addEdge('a', 'c', 2)
    g.addEdge('c', 'b', 3)
    g.addEdge('b', 'd', 1)
    g.addEdge('c', 'd', 5)
    g.addEdge('d')
    g.calculate()
    print(g.graph)
    print(g.cost)
    print(g.father)