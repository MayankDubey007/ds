class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def  insert(self,data):
        if data < self.data:
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.insert(data)
    
    def display(self):
        if self.left:
            self.left.display()
        print(self.data,end=",")
        if self.right:
            self.right.display()
    
    def search(self,key):
        if key < self.data:
            if self.left == None:
                return "Not Found"
            return self.left.search(key)
        elif key > self.data:
            if self.right == None:
                return "Not Found"
            return self.right.search(key)
        else:
            return "key found in tree"
    def inorder(self,root):
        result = []
        if root:
            result = self.inorder(root.left)
            result.append(root.data)
            result = result + self.inorder(root.right)
        return result
    def preorder(self,root):
        result = []
        if root:
            result.append(root.data)
            result = result + self.preorder(root.right)
            print(result)
            result = self.preorder(root.left)
        return result
    def postorder(self,root):
        result = []
        if root:
            result = self.postorder(root.left)
            result.append(root.data)
            result = result + self.postorder(root.right)
        return result
root = Node(4)
root.insert(7)
root.insert(2)
root.insert(3)
root.insert(1)
root.insert(5)
root.insert(6)
# root.display()
print(root.preorder(root))  
print(root.inorder(root))
print(root.postorder(root))