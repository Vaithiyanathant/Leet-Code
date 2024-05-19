class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans = 0
        low = 0
        high = len(nums)-1    
        while(low<=high):
            if low==high:
                ans+=nums[low]
                low +=1
                high-=1
            else:
                ans+=int(str(nums[low])+str(nums[high]))
                low+=1
                high-=1
        print(ans)    
        return ans