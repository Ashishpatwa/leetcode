class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        
        intervals.sort(key=lambda x:x[1])
        count=0
        start=0
        end=1
        prev=intervals[0]
        
        for i in range(1,len(intervals)):
            curr=intervals[i]
            if prev[end]<=curr[start]:
                prev=curr
            else:
                count+=1
        return count
        