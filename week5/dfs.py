class TreeNode:
    def __init__ (self,value,left=None,right=None):
        self.value=value
        self.left=None
        self.right=None


    def dfsIteration(root):
        stack=[root]
        visited=set()
        if root is None:
            return []
        while stack:
            node=stack.pop()
            if node and node not in visited:
                visited.add(node)
                if node.right not None:
                    stack.append(node.right)
                if node.left not None:
                    stack.append(node.left)
        return visited





# def recursive(graph,start):
#     visited=set()
#     stack=[start]
#     if start == None:
#         return []
#     root.left= recursive(root.left) # all left values
#     root.right=recursive(root.right) # all right values

#     return [root,root.left,root.right]
    





    