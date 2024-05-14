class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        rem = [ ]
        for i in nums:
            rem.append(int(str(i)[::-1]))
        return len(set(nums+rem))
        