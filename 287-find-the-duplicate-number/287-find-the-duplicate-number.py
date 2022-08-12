class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # negative marking o(n) o(1) 
        # for i in range(len(nums)):
        #     v= abs(nums[i])
        #     if nums[v]<0:
        #         return v
        #     nums[v]*=-1
        
        # cycle detection o(n) o(1)
        fast=nums[0]
        slow=nums[0]
        
        while True:
            fast= nums[nums[fast]]
            slow= nums[slow]
            if fast==slow:
                break
        
        slow=nums[0]
        while fast!=slow:
            fast=nums[fast]
            slow=nums[slow]
        return fast
        
        