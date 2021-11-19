class node:
    def __init__(self,data = None):
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
    def _inorder(self,current):
        if current:
            self._inorder(current.left_node)
            print(current.data,end=" ")
            self._inorder(current.right_node)
    def preorder(self):
        if(self.root == None):
            print("Tree Is Empty....")
        else:
            self._preorder(self.root)
    def _preorder(self,current):
        if current:
            print(current.data,end=" ")
            self._preorder(current.left_node)
            self._preorder(current.right_node)
    def postorder(self):
        if(self.root == None):
            print("Tree Is Empty....")
        else:
            self._postorder(self.root)
    def _postorder(self,current):
        if current:
            self._postorder(current.left_node)
            self._postorder(current.right_node)
            print(current.data,end=" ")
    def ADD(self,val):
        if(self.root == None):
            self.root = node(val)
        else:
            self._ADD(self.root,val)
    def _ADD(self,current,val):
        if(current.data > val):
            if(current.left_node==None):
                current.left_node = node(val)
            else:
                self._ADD(current.left_node,val)
        elif(current.data < val):
            if(current.right_node == None):
                current.right_node = node(val)
            else:
                self._ADD(current.right_node,val)
        else:
            print("value is Already Added in the Three....")            
ob1 = BinarySearchTree()
ob1.ADD(50)
ob1.ADD(10)
ob1.ADD(20)
ob1.ADD(30)
ob1.ADD(40)
ob1.ADD(60)
ob1.inorder()
print()
ob1.preorder()
print()
ob1.postorder()
print()