class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)
        
        # Calculate the maximum and minimum values in the list
        maxi = max(nums)
        mini = min(nums)
        return gcd(maxi,mini)