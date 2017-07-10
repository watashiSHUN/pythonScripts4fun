# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        returnV = None
        if t1 or t2:
            returnV = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
            returnV.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
            returnV.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return returnV
