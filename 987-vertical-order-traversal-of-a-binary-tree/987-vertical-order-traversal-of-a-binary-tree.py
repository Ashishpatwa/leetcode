# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dic=dict()
        self.bfs(root,dic,0)
        ans=[]
        k=dic.keys()
        k.sort()
        for i in k:
            ans.append(dic[i])
        return ans
    def bfs(self,root,dic,d):
        queue=deque()
        queue.append([root,d])
        while queue:
            ln=len(queue)
            tmp_dict=dict()
            for i in range(ln):
                rt,ind=queue.popleft()
                if rt.left:
                    queue.append([rt.left,ind-1])
                if rt.right:
                    queue.append([rt.right,ind+1])
                if ind in tmp_dict:
                    insort(tmp_dict[ind],rt.val)
                else:
                    tmp_dict[ind]=[rt.val]
            
            for i in tmp_dict:
                if i in dic:
                    for j in tmp_dict[i]:
                        dic[i].append(j)
                else:
                    dic[i]=tmp_dict[i]
                
                    
        