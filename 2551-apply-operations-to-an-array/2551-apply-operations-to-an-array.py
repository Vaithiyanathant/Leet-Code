class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        zer = 0
        print(nums)
        for i in range(len(nums)):
            if nums[i] !=0:
                t = nums[zer]
                nums[zer] = nums[i]
                nums[i] = t
                zer+=1
        return nums

        
