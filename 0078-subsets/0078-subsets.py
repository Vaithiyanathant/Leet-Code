class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lst = [[]]
        n = len(nums)
        for i in range(1,2**n):
            k = []
            for j in range(len(nums)):
                if (i & 1<<j):
                    k.append(nums[j])
            lst.append(k)
        return lst