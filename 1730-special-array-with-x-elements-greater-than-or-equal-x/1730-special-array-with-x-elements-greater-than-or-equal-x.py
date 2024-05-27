class Solution:
    def specialArray(self, nums: List[int]) -> int:
        def helper(kathija):
            kanmani = 0
            for i in range(len(nums)):
                if kathija<=nums[i]:
                    kanmani+=1
            return kanmani
        
        low = 0
        high = 100
        while(low<=high):
            mid = (low+high)//2
            if helper(mid)==mid:
                return mid
            elif mid<helper(mid):
                low = mid+1
            elif mid >helper(mid):
                high = mid-1
        return -1
    


        