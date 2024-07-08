class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        if len(nums)==2:
            return nums
        else:
            olst = []
            elst = []
            for i in range(len(nums)):
                if i%2==0:
                    elst.append(nums[i])
                else:
                    olst.append(nums[i])
            olst = sorted(olst)[::-1]
            elst = sorted(elst)
            o = 0
            e = 0
            res = []
            for i in range(len(nums)):
                if i%2 == 0:
                    nums[i] = elst[e]
                    e+=1
                else:
                    nums[i]= olst[o]
                    o+=1
            return nums
            


                
        