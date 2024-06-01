class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ma = 0
        pre = 0
        for i in gain:
            pre+=i
            ma = max(pre,ma)
        return ma

        
        