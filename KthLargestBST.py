class BST:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def insert(self,data):
        if self is None:
            self.data=data
            return
        if self.data==data:
            return
        if data < self.data:
            if self.left is None:
                self.left=BST(data)
                return
            self.left.insert(data)
            return
        if self.right is None:
            self.right=BST(data)
            return
        self.right.insert(data)
        return
    def reverseinOrderTraversal(self):
        if self is None:
            return
        datas=[]
        if self.right is not None:
            datas+=self.right.reverseinOrderTraversal()
        datas.append(self.data)
        if self.left is not None:
            datas+= self.left.reverseinOrderTraversal()
        
        return datas
    def KthLargestElement(self,k):
        val=self.reverseinOrderTraversal()
        print (val)
        return val[k-1]

        
bst=BST(12)
bst.insert(3)
bst.insert(5)
bst.insert(11)
bst.insert(13)
bst.insert(25)
bst.insert(21)
bst.insert(33)
bst.insert(53)
bst.insert(61)
bst.insert(45)
bst.insert(65)
bst.insert(42)
print(bst.KthLargestElement(6))