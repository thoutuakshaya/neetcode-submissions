class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        first=1
        s=nums[0]
        m=nums[0]
        for i in range(first,len(nums)):
            if nums[i]>nums[i-1]:
                s+=nums[i]
                
            else:
                s=nums[i]
                first=i
            m=max(m,s)
        return m