# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans=0
        self.recursion(root,0,low,high)
        return self.ans
    def recursion(self,root,i,low,high):
        if root==None:
            return 0
        
            
        self.recursion(root.left,i,low,high)
        if root.val>=low and root.val<=high:
            self.ans+=root.val
        self.recursion(root.right,i,low,high)
        
        
        