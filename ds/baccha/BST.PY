class node:
    def __init__(self, data=None):
        self.data = data
        self.Lnode = None
        self.Rnode = None


class BST:
    def __init__(self):
        self.root = None

    def inorder(self):
        if(self.root == None):
            print("tree is empty....")
        else:
            self._inorder(self.root)
            print()

    def _inorder(self, current):
        if current:
            self._inorder(current.Lnode)
            print(current.data, end=",")
            self._inorder(current.Rnode)

    def preorder(self):
        if(self.root == None):
            print("tree is empty....")
        else:
            self._preorder(self.root)
            print()

    def _preorder(self, current):
        if current:
            print(current.data, end=",")
            self._preorder(current.Lnode)
            self._preorder(current.Rnode)

    def postorder(self):
        if(self.root == None):
            print("tree is empty....")
        else:
            self._postorder(self.root)
            print()

    def _postorder(self, current):
        if current:
            self._postorder(current.Lnode)
            self._postorder(current.Rnode)
            print(current.data, end=",")

    def levelorder(self):
        if(self.root == None):
            print("tree is Empty")
        else:
            self._levelorder(self.root)

    def _levelorder(self, current):
        queue = []
        queue.append(current)
        while len(queue) > 0:
            node1 = queue.pop(0)
            print(node1.data, end=",")
            if(node1.Lnode is not None):
                queue.append(node1.Lnode)
            if(node1.Rnode is not None):
                queue.append(node1.Rnode)

    def addnode(self, val):
        if(self.root == None):
            self.root = node(val)
        else:
            self._addnode(self.root, val)

    def _addnode(self, current, val):
        if(current.data > val):
            if(current.Lnode == None):
                current.Lnode = node(val)
            else:
                self._addnode(current.Lnode, val)
        elif(current.data < val):
            if(current.Rnode == None):
                current.Rnode = node(val)
            else:
                self._addnode(current.Rnode, val)
        else:
            print('value is already add in this Tree...')


obj = BST()
obj.addnode(10)
obj.addnode(5)
obj.addnode(15)
obj.addnode(2)
obj.preorder()
obj.inorder()
obj.postorder()
obj.levelorder()
