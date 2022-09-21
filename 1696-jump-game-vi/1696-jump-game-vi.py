class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        dp=[0]*len(nums)
        dp[0]=nums[0]
        heap=[]
        heapq.heappush(heap,[-nums[0],0])
        for i in range(1,len(nums)):
            while heap and heap[0][1]<i-k:
                heapq.heappop(heap)
            mx=heap[0]
            dp[i]=-mx[0]+nums[i]
            heapq.heappush(heap,[-dp[i],i])
        return dp[-1]
            
        
        
        