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
    def max_product(self):
        sum=[]
        subtree_1_sums=[]
        def tree_sum(subroot):
            if subroot is None:
                return 0
            left_sum=tree_sum(subroot.left)
            right_sum=tree_sum(subroot.right)
            tree_sum=subroot.data+left_sum+right_sum
            return sum.append(tree_sum)
        total_sum=tree_sum(self)
        max_product=0
        for subtree_1_sum in sum:
            subtree_2_sum=total_sum-subtree_1_sum
            product=subtree_1_sum*subtree_2_sum
            max_product=max(product,max_product)
        return  (max_product)% (10 ** 9 + 7)
    
bst=BST(34)
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
bst.max_product()
