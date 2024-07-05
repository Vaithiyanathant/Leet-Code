class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(set(nums))<=2:
            return -1
        return sorted(nums)[1]
        