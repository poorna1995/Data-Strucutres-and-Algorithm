class BST():
    def __init__(self):
        self.val=val
        self.left=None
        self.right=None
    def insert(self,root,val):
        if root == None:
            return BST(val)
        if val < root.val:
            root.left= BST.insert(self,root.left,val)
        else val >root.val:
            root.right= BST.insert(self,root.right,val)
        return root

        

       