# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.dic=dict()
        self.count=0
        self.recursion(root)
        return self.count
    def recursion(self,root):
        if root==None:
            return root
        if root.left==None and root.right==None:
            self.dic[root.val]=self.dic.get(root.val,0)+1
            if self.checker():
                self.count+=1
            self.dic[root.val]-=1
            return
        self.dic[root.val]=self.dic.get(root.val,0)+1
        self.recursion(root.left)
        self.recursion(root.right)
        self.dic[root.val]-=1
    def checker(self):
        cnt=0
        
        for i in self.dic.values():
            if i%2!=0:
                cnt+=1
        return False if cnt>1 else True