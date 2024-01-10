class BSTNode:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None
    def insert(self,data):
        if self.data==data:
            return
        if not self.data:
            self.data=data
            return
        if data < self.data:
            if self.left:
                self.left.insert(data)
                
            else:
                self.left=BSTNode(data)
            
        else:
            if self.right:
                self.right.insert(data)
            else:    
                self.right=BSTNode(data)
    def delete(self,data):
        
        if data<self.data:
            if self.left:
                self.left.delete(data)
        elif data>self.data:
            if self.right:
                self.right.delete(data)
        else:
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            
            current=self.right.getMin()
            self.data=current
            self.right=self.right.delete(current)
        return self
    def search(self,data):
        if data==self.data:
            return True
        if data<self.data:
            if self.left==None:
                return False
            return self.left.search(data)
        if data>self.data:
            if self.right==None:
                return False
            return self.right.search(data)





    def getMin(self):
        itr=self
        while itr.left is not None:
            itr=itr.left
        return itr.data
    def getMax(self):
        itr=self
        while itr.right is not None:
            itr=itr.right
        return itr.data
    def inOrder(self):
        datas=[]
        if self.left is not None:
            datas+=self.left.inOrder()
        
        datas.append(self.data)
        
        if self.right is not None:
            datas+=self.right.inOrder()
        return datas
    def preOrder(self):
        datas=[]
        datas.append(self.data)
        if self.left is not None:
            datas+=self.left.preOrder()
        if self.right is not None:
            datas+=self.right.preOrder()
        return datas

values=[2,10,9,7,6,14,1,5,15,18]
bst=BSTNode(12)
for num in values:
    bst.insert(num)

print("Printing tree values is inOrder",bst.inOrder())
print("Printing tree values is preOrder",bst.preOrder())
print ("Maximum value of this BST is ",bst.getMax())
print ("Minimum value of this BST is ",bst.getMin())
#bst.delete(2)
print ("deleting value of this BST is ",bst.search(14))

