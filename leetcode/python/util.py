# -*- coding: utf-8 -*-
"""LeetCode Util tools

Provide utility tools for local debuggings of leetcode questions. 

"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


null = "null"


class UtilFuncs:
    """makeTreeNode
    
    make input arrays to TreeNode
        
    Args:
        nums (list[int]) input integer array representing tree nodes
    """
    @staticmethod
    def makeBinaryTree(nums) -> TreeNode:
        def treeify(i):
            root = TreeNode(val=nums[i])
            li, ri = 2*i+1, 2*i+2
            if li < len(nums) and nums[li] not in ["null", None]:
                root.left = treeify(li)
            if ri < len(nums) and nums[ri] not in ["null", None]:
                root.right = treeify(ri)

            return root

        return treeify(0)
