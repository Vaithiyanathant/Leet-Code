class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a,b):
            if a  < b :
                return gcd(b,a)
            if b == 0:
                return a
            return gcd(b,a%b)
        ma = max(nums)
        mi = min(nums)
        return gcd(ma,mi)
        