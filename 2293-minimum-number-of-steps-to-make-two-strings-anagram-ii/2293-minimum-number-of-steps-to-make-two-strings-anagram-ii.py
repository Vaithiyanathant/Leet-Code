class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d = Counter(s)
        d2 = Counter(t)
        res = 0
        for i in "abcdefghijklmnopqrstuvwxyz":
            d[i]-=d2[i]
        for i in d:
            res+=abs(d[i])
        print(d)
        return res
        
        