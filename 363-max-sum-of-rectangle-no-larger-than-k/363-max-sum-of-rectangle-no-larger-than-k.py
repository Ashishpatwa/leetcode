class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        mx=-float('inf')
        for left in range(len(matrix[0])):
            arr=[0]*len(matrix)
            for right in range(left,len(matrix[0])):
                for row in range(len(matrix)):
                    arr[row]+=matrix[row][right]
                st=[0]
                cs=0
                for i in arr:
                    cs+=i
                    currmax = bisect_left(st,cs-k)
                    if currmax<len(st):
                        if st[currmax]==cs-k:
                            return k
                        else:
                            mx=max(mx,cs-st[currmax])
                    insort(st, cs)
                    
        return mx

                    