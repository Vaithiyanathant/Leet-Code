class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        n = len(nums)
        for i in range(n):
            r = target - nums[i]
            if r in m:
                return [m[r],i]
            m[nums[i]]=i
        return []
