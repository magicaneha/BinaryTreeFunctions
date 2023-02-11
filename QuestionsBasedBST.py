#find the kth smallest element is the BST

class BSTNode:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None
    def insert(self,data):
        if self is None:
            self.data=data
            return
        if self.data==data:
            return
        if self.data >  data:
            if self.left is None:
                self.left=BSTNode(data)
                return
            self.left.insert(data)
            return
        if self.right is None:
            self.right=BSTNode(data)  
            return
        self.right.insert(data)
        return
    def getMin(self):
        itr=self
        while itr:
            itr=itr.left
        return itr.data
    def inOrderTraversal(self):
        datas=[]
        if self.left is not None:
            datas+= self.left.inOrderTraversal()
        datas.append(self.data)
        if self.right is not None:
            datas+=self.right.inOrderTraversal()
        return datas

    def findKthSmallest(self,k):
        value=self.inOrderTraversal()
        print(value[k-1])
        
bst=BSTNode(5)
bst.insert(2)
bst.insert(1)
bst.insert(6)
bst.insert(3)
bst.insert(7)
bst.insert(8)
bst.insert(2)
bst.insert(11)
bst.insert(16)
bst.insert(23)
bst.insert(37)
bst.insert(38)
bst.findKthSmallest(8)






