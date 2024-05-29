class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxii = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    maxii = max(maxii,(nums[i] - nums[j]) * nums[k])
        return maxii

        