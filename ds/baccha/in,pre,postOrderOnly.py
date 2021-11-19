class node:
    def __init__(self, data=None):
        self.data = data
        self.Lnode = None
        self.Rnode = None
class BinaryTree:
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
            print(current.data,end=",")
            self._inorder(current.Rnode)
    def preorder(self):
        if(self.root == None):
            print("tree is empty....")
        else:
            self._preorder(self.root)
            print()

    def _preorder(self, current):
        if current:
            print(current.data,end=",")
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
            print(current.data,end=",")


obj = BinaryTree()
first = node(1)
second = node(2)
third = node(3)
fourth = node(4)
fifth = node(5)
sixth = node(6)
seventh = node(7)
obj.root = first
first.Lnode = second
first.Rnode = third
second.Lnode = fourth
second.Rnode = fifth
third.Lnode = sixth
third.Rnode = seventh
obj.inorder()
obj.preorder()
obj.postorder()
