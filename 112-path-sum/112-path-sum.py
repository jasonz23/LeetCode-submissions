# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        if root.left == None and root.right == None:
            return root.val == targetSum
        left = False
        right = False
        if root.left != None:
            left = self.hasPathSum(root.left,targetSum - root.val)
        
        if root.right != None:
            right = self.hasPathSum(root.right, targetSum - root.val)
        return left or right
        