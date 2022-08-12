class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # i=0
        # while nums[nums[i]]>0:
        #     nums[nums[i]]*=-1
        #     i=abs(nums[nums[i]])
        # return abs(nums[i])
        
        for i in range(len(nums)):
            v= abs(nums[i])
            if nums[v]<0:
                return v
            nums[v]*=-1
        