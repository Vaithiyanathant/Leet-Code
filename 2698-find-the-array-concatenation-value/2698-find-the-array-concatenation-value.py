class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        print()
        i = 0
        j = len(nums)-1
        res = 0
        while(i <= j):
            if i==j:
                res+=nums[i]
                break
            tw = floor((math.log10(nums[j])+1))
            res  = res + nums[i]*(10**tw) + nums[j]
            i+=1
            j-=1
        return res 
            
        