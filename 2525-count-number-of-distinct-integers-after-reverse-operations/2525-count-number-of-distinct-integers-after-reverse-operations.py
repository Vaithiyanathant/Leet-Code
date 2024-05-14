class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        rem = [ ]
        for i in nums:
            rem.append(int(str(i)[::-1]))
        print(rem)
        return len(set(nums+rem))
        