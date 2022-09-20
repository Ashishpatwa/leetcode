class Solution:
    def jump(self, nums: List[int]) -> int:
        arr=[float('inf')]*len(nums)
        arr[-1]=0
        for i in range(len(nums)-2,-1,-1):
            max_len=min(i+nums[i],len(nums)-1)
            arr[i]=min(arr[i:max_len+1])+1
        print(arr)
        return arr[0]
                
        