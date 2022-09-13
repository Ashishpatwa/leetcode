class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        adj= {i:[] for i in range(n)}
        indegree= {i:0 for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u]+=1
            indegree[v]+=1
            
        queue=deque()
        for i in range(n):
            if indegree[i]==1:
                queue.append(i)
        count=0
        ans=[]
        while n-count>2:
            ln=len(queue)
            for i in range(ln):
                count+=1
                ele=queue.popleft()
                for i in adj[ele]:
                    indegree[i]-=1
                    if indegree[i]==1:
                        queue.append(i)
        return queue
            
                    
                
            
        