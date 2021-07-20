class bTree:
    def __init__(self):
        self.root = None

    def Insert(self, value):
        print(value)
        if self.root == None:
            self.root = Node(value)
            return
        else:
            node = self.root
            while True:
                parent = node
                node = node.right if parent.value < value else node.left
                if node == None:
                    node = Node(value)
                    if parent.value < value:
                        parent.right = node
                    else:
                        parent.left = node
                    return

    def DeleteMax(self):
        if self.root == None:
            return
        if self.root.right == None:
            self.root = self.root.left
            return

        parent = None
        node = self.root
        while node.right != None:
            parent = node
            node = node.right
        parent.right = node.left

    def DeleteMin(self):
        if self.root == None:
            return
        if self.root.left == None:
            self.root = self.root.right
            return

        parent = None
        node = self.root
        while node.left != None:
            parent = node
            node = node.left

        parent.left = node.right

    def getMax(self):
        if self.root == None:
            return

        parent = None
        node = self.root
        while node.right != None:
            parent = node
            node = node.right

        return node.value

    def getMin(self):
        if self.root == None:
            return

        parent = None
        node = self.root
        while node.left != None:
            parent = node
            node = node.left

        return node.value

    def IsEmpty(self):
        return self.root == None



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def solution(operations):
    tree = bTree()
    for i in operations:
        if i.startswith("I"):
            value = int(i.split()[1])
            tree.Insert(value)
        elif i == "D 1":
            tree.DeleteMax()
        elif i == "D -1":
            tree.DeleteMin()

    if tree.IsEmpty():
        return [0, 0]
    else:
        return [tree.getMax(), tree.getMin()]