class TreeNode:
    def __init__ (self,val,left,right):
        self.val = val
        self.left = left
        self.right = right

    def BreadthSearchTree(root):
        queue=[start]
        visited=[]

        if start is None:
            return []
        while queue:
            node= queue.pop(0)
            visited.append(node.val)

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        return visited


