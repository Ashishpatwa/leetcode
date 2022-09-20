class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue=deque()
        queue.append(start)
        
        while queue:
            ln=len(queue)
            for i in range(ln):
                ky=queue.popleft()
                if arr[ky]==0:
                    return True
                if arr[ky]<0:
                    continue
                if ky+arr[ky]<len(arr):
                    queue.append(ky+arr[ky])
                if ky-arr[ky]>=0:
                    queue.append(ky-arr[ky])
                arr[ky]=-arr[ky]
        return False
                
                    
        
        