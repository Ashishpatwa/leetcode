class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        left=defaultdict(int)
        dic=Counter(nums)
        
        for i in nums:
            if not dic[i]:
                continue
            if left[i-1]>0:
                left[i-1]-=1
                left[i]+=1
                dic[i]-=1
            else:
                if not dic[i+1] or not dic[i+2]:
                    return False
                dic[i]-=1
                dic[i+1]-=1
                dic[i+2]-=1
                left[i+2]+=1
        return True
    