class Solution:
    def countElements(self, nums: List[int]) -> int:
        mi = 99999
        ma = 99999*-1
        for i in nums:
            mi = min(mi,i)
            ma  = max(ma, i)
        nums.sort()
        got = 0
        for i in range(1,len(nums)-1):
            if mi < nums[i] < ma:
                got+=1
        return got
