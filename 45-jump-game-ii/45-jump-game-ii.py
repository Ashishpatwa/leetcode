class Solution:
    def jump(self, nums: List[int]) -> int:

        # arr=[float('inf')]*len(nums)
        # arr[-1]=0
        # for i in range(len(nums)-2,-1,-1):
        #     max_len=min(i+nums[i],len(nums)-1)
        #     arr[i]=min(arr[i:max_len+1])+1
        # return arr[0]
        if len(nums)==1:
            return 0
        e=nums[0]
        j=1
        mr=nums[0]
        
        for i in range(1,len(nums)-1):
            mr=max(mr,i+nums[i])
            if i==e:
                j+=1
                e=mr
        return j
                
        