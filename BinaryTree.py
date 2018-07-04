from Debug import inputLog
from Debug import outputLog
from Debug import DebugSetting

class Leaf:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

    Debug = DebugSetting()['BinaryTree']

    def __init__(self):
        self.root = None

    @inputLog(Debug)
    def insert(self, data):
        if self.root == None:
            self.root = Leaf(data)
        else:
            self.__insert(self.root, data)

    def __insert(self, leaf, data):
        if leaf.data > data:
            if leaf.left != None:
                self.__insert(leaf.left, data)
            else:
                leaf.left = Leaf(data)
        elif leaf.data < data:
            if leaf.right != None:
                self.__insert(leaf.right, data)
            else:
                leaf.right = Leaf(data)
        else:
            print('--- repeat data ---')

    def inOrder(self):
        print('--- inorder ---')
        self.__inOrder(self.root)

    def preOrder(self):
        print('--- pre order ---')
        self.__preOrder(self.root)

    def postOrder(self):
        print('--- post order ---')
        self.__postOrder(self.root)

    def __inOrder(self, leaf):
        if leaf.left != None:
            self.__inOrder(leaf.left)
        print(leaf.data)
        if leaf.right != None:
            self.__inOrder(leaf.right)

    def __preOrder(self, leaf):
        print(leaf.data)
        if leaf.left != None:
            self.__preOrder(leaf.left)
        if leaf.right != None:
            self.__preOrder(leaf.right)

    def __postOrder(self, leaf):
        if leaf.left != None:
            self.__postOrder(leaf.left)
        if leaf.right != None:
            self.__postOrder(leaf.right)
        print(leaf.data)


if __name__ == "__main__":
    t = BinaryTree()
    t.insert(5)
    t.insert(1)
    t.insert(4)
    t.insert(7)
    t.insert(10)

    t.inOrder()
    t.preOrder()
    t.postOrder()

    #    5
    #  1   7
    #   4    10

