class node:
    def __init__(self, data=None):
        self.data = data
        self.left_node = None
        self.right_node = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def inorder(self):
        if(self.root == None):
            print("Tree Is Empty....")
        else:
            self._inorder(self.root)

    def _inorder(self, current):
        if current:
            self._inorder(current.left_node)
            print(current.data, end=" ")
            self._inorder(current.right_node)

    def preorder(self):
        if(self.root == None):
            print("Tree Is Empty....")
        else:
            self._preorder(self.root)

    def _preorder(self, current):
        if current:
            print(current.data, end=" ")
            self._preorder(current.left_node)
            self._preorder(current.right_node)

    def postorder(self):
        if(self.root == None):
            print("Tree Is Empty....")
        else:
            self._postorder(self.root)

    def _postorder(self, current):
        if current:
            self._postorder(current.left_node)
            self._postorder(current.right_node)
            print(current.data, end=" ")

    def addnode(self, val):
        if(self.root == None):
            self.root = node(val)
        else:
            self._addnode(self.root, val)

    def levelorder(self):
        if(self.root == None):
            print("Tree Is Empty....")
        else:
            self._levelorder(self.root)

    def _levelorder(self, current):
        queue = []
        queue.append(current)
        while len(queue) > 0:
            node1 = queue.pop(0)
            print(node1.data, end=" ")
            if(node1.left_node is not None):
                queue.append(node1.left_node)
            if(node1.right_node is not None):
                queue.append(node1.right_node)

    def _addnode(self, current, val):
        if(current.data > val):
            if(current.left_node == None):
                current.left_node = node(val)
            else:
                self._addnode(current.left_node, val)
        elif(current.data < val):
            if(current.right_node == None):
                current.right_node = node(val)
            else:
                self._addnode(current.right_node, val)
        else:
            print('Value is Already Added in The tree..')

    def deleteNode(self.root, data):
        root = self.root 
        if root is None:
            return root
        if data < root.data:
            root.left_node = self.deleteNode(root.left_node, data)
            return root

        elif(data > root.data):
            root.right_node = self.deleteNode(root.right_node, data)
            return root
        if root.left_node is None and root.right_node is None:
            return None
        if root.left_node is None:
            temp = root.right_node
            root = None
            return temp
        elif root.right_node is None:
            temp = root.left_node
            root = None
            return temp
        succParent = root
        succ = root.right_node
        while succ.left_node != None:
            succParent = succ
            succ = succ.left_node
        if succParent != root:
            succParent.left_node = succ.right_node
        else:
            succParent.right_node = succ.right_node
        root.data = succ.data
        return root


ob1 = BinarySearchTree()
ob1.addnode(60)
ob1.addnode(50)
ob1.addnode(40)
ob1.addnode(400)
ob1.addnode(30)
ob1.addnode(20)
ob1.addnode(10)
ob1.deleteNode(30)
ob1.inorder()
print()
ob1.preorder()
print()
# ob1.inorder()
# print()
ob1.postorder()
print()
