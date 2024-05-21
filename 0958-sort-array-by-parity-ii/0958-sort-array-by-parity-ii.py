class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i = 0
        j = 1
        res = [0]*len(nums)
        for k in nums:
            if k%2==0:
                res[i]=k
                i+=2
            else:
                res[j]=k
                j+=2
        return res



        