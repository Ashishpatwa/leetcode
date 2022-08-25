class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        count=0
        curr_day=1
        heap=[]
        i=0
        while i<len(apples) or heap:
            if i<len(apples):
                heapq.heappush(heap,[days[i]+i+1, apples[i]])
          
            while heap and (heap[0][1]==0 or curr_day>=heap[0][0]) :
                heapq.heappop(heap)
            if heap:
                curr = heap[0]
                heapq.heappop(heap)
                if curr[1]-1>0:
                    heapq.heappush(heap,[curr[0], curr[1]-1])
                count+=1
            curr_day+=1
            i+=1
        return count
