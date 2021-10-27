# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class MinDepth:
    def __init__(self):
        self.leaf = 0
    
    def deeper2(self, currentDepth: int, currentNode) -> int:
        c = currentDepth
        l,r = c,c 

        if currentNode.left is None and currentNode.right is None:
            if self.leaf == 0 or self.leaf > c:
                self.leaf = c
            return c

        if currentNode.left != None:
            l = self.deeper2(c+1, currentNode.left)

        if currentNode.right != None:
            r = self.deeper2(c+1, currentNode.right)

        return l if r < l else r

    def minDepth(self, root) -> int:
        if root == None:
            return 0

        self.deeper2(1, root)
        return self.leaf


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class MaxDepth:
    def deeper(self, currentDepth: int, currentNode) -> int:
        c = currentDepth
        l,r = c,c 

        if currentNode.left != None:
            l = self.deeper(c+1, currentNode.left)

        if currentNode.right != None:
            r = self.deeper(c+1, currentNode.right)

        return l if r < l else r

    def maxDepth(self, root) -> int:
        if root == None:
            return 0

        return self.deeper(1, root)

