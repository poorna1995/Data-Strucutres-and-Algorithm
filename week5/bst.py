class binarySearchTree:
    def __init__ (self,key):
        self.left=None
        self.right=None
        self.value=key
    
    def insert(root,key):
        if root is None:
            return binarySearchTree(key)

        if key<root.value:
            root.left=binarySearchTree.insert(root.left,key)
        else:
            root.right=binarySearchTree.insert(root.right,key)
        return root
        
    def inOrderTraversal(root):
        if root:
            binarySearchTree.inOrderTraversal(root.left)
            print(root.value)
            binarySearchTree.inOrderTraversal(root.right)
    
    def delete(key):
        # """
        # The provided function attempts to delete a node with a specific key from a binary search tree,
        # handling cases where the node has one child or no child.
        
        # :param key: The code snippet you provided is a recursive function to delete a node with a
        # specific key from a binary search tree. It seems like there are a few issues in the code that
        # need to be addressed:
        # :return: The code snippet is attempting to delete a node with a specific key from a binary search
        # tree. The function is recursively called to traverse the tree and find the node with the given
        # key to delete. If the node is found, its value is deleted. If the node has one child or no child,
        # the appropriate child is assigned to the parent node. Finally, if the node has two children, the
        # """

        if root is None:
            return 0
        if root.val == key:
            delete(root.val)
        if root.val > key:
            root.left= delete(root.left,key)
        elif root.val>key
            root.right=delete(root.right,key)
        else:

            # if the root has a one children or no children
            if root.left or root.right is None:
                temp = root.left or root.right
                root= None
                return temp

            # if the rooth has two children then fin the smallest value of the right of the root 
            if root.left and root.right is not None:
                temp = minValueNode(root.right)
                root.val=temp.val

                root.right=delete(root.right,temp.val)





    #     if root is None:
    #         return 0
    #     if root.val==key:
    #         del (root.val)
    #    # The code snippet you provided is attempting to delete a node with a specific key from a
    #    # binary search tree.
    #     if root.val>key:
    #         root.left=delete(root.left,key)
    #     elif  root.val<key:
    #         root.right=delete(root.right,ley)
    #     # This part of the code snippet is handling the case where the node to be deleted has one
    #     # child or no child.
    #     else:
    #         if root.left is None:
    #             temp =root.right
    #             root=None
    #             return temp
    #         elif root.right is None:
    #             temp =root.left
    #             root=None
    #             return temp
    #     temp = minValueNode(root.right)
    #     root.val=temp.val

    #     root.right=delete(root.right,temp.val)

def minValueNode(node):
    current=node
    while current.left is not None:
        current=current.left
    return current
            
           
            








if __name__=='__main__':
    r = binarySearchTree(5)
    r = binarySearchTree.insert(r, 6)
    r = binarySearchTree.insert(r, 2)
    r = binarySearchTree.insert(r, 7)
    r = binarySearchTree.insert(r, 1)
    r = binarySearchTree.insert(r, 10)

print( binarySearchTree.inOrderTraversal(r))





