# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if self.sameTree(root,subRoot):
            return True;
        b1 = self.isSubtree(root.left,subRoot)
        
        b2 = self.isSubtree(root.right,subRoot)
        return b1 or b2
        
    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False
        return (p.val == q.val) and self.sameTree(p.left,q.left) and self.sameTree(p.right,q.right)
        
        