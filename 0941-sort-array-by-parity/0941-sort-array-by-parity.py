class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        low = 0
        high = len(nums)-1
        while(low<high):
            if nums[low]%2==1 and nums[high]%2==0:
                temp = nums[low]
                nums[low]=nums[high]
                nums[high]=temp
                low+=1
                high-=1
            elif nums[low]%2==0 and nums[high]%2==1:
                low+=1
                high-=1
            elif nums[low]%2==0 and nums[high]%2==0:
                low+=1
            elif nums[low]%2==1 and nums[high]%2==1:
                high-=1
        return nums


        