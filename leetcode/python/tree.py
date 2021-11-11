# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

null = "null"

"""
leetcode util function make input arrays to TreeNode
"""
def makeTreeNode(nums) -> TreeNode:
    def treeify(i):
        root = TreeNode(val=nums[i])
        li, ri = 2*i+1, 2*i+2
        if li < len(nums) and nums[li] not in ["null", None]:
            root.left = treeify(li)
        if ri < len(nums) and nums[ri] not in ["null", None]:
            root.right = treeify(ri)

        return root

    return treeify(0)


class LevelOrder:
    def dfs(self, root: TreeNode, depth, values):
        if root is None:
            return

        if len(values)-1 < depth:
            values.append([root.val])
        else:
            values[depth].append(root.val)

        self.dfs(root.left, depth+1, values)
        self.dfs(root.right, depth+1, values)
        return values

    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        return self.dfs(root, 0, [[]])

# first solution using instance global dictionary
# class Solution:
#    def dfs(self, root: TreeNode, depth):
#        if root is None:
#            return
#
#        if depth not in self.ord:
#            self.ord[depth] = []
#
#        self.ord[depth].append(root.val)
#        self.dfs(root.left, depth+1)
#        self.dfs(root.right, depth+1)
#
#
#    def levelOrder(self, root: TreeNode) -> list[list[int]]:
#        self.ord = {}
#        self.dfs(root, 0)
#
#        return [ val for _, val in sorted(self.ord.items(), key=lambda x:x[0])]


if __name__ == "__main__":
    l = LevelOrder()
    print(l.levelOrder(makeTreeNode([3,9,20,null,null,15,7])))
