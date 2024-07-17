class TreeNode:
    def __init__(self,val,left,right):
        self.value = val
        self.left = left
        self.right = right
    
    def treeSum(root):
        if root is None:
            return 0
        
        queue=[root]
        visited=[]
        sum=0
        while queue:
            node= queue.pop(0)
            visited.append(node)
            sum+=node

            if node.left not None:
                queue.append(node.left)
            if node.right not None:
                queue.append(node.right)
        
        return sum



