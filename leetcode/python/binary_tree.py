# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

##########################################

# https://leetcode.com/problems/path-sum
class HasPathSum:
    def isLeaf(self, node): 
        return node.left == None and node.right == None

    def hasPathSum(self, root, targetSum: int) -> bool:
        if root == None:
            return False

        nextTarget = targetSum - root.val
        if nextTarget == 0 and self.isLeaf(root):
            return True

        return self.hasPathSum(root=root.left, targetSum=nextTarget) or self.hasPathSum(root=root.right, targetSum=nextTarget)

# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
class SortedArrayToBST:
    def sortedArrayToBST(self, nums: list[int]):
        if len(nums) < 1:
            return None

        r = len(nums) // 2
        print(r, nums[r])
        root =  TreeNode(val=nums[r])

        if len(nums) > 1:
            root.left = self.sortedArrayToBST(nums[:r])
            root.right = self.sortedArrayToBST(nums[r+1:])

        return root


# https://leetcode.com/problems/merge-two-binary-trees
class MergeTrees:
    def mergeTrees(self, root1, root2):
        if root1 == None:
            return root2
        if root2 == None:
            return root1

        root = TreeNode(val=root1.val + root2.val)
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)

        return root
        

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

if __name__ == "__main__":
    s = SortedArrayToBST()
    assert(s.sortedArrayToBST([1,3]) == [1,3])

