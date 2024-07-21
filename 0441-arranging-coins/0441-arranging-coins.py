class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 0
        high = 2**31 -1
        while(low<=high):
            mid = (low+high)//2
            if n==(mid*(mid+1)//2):
                return mid
            if n>(mid*(mid+1))//2:
                low = mid+1
            else:
                high = mid-1
        return high

        