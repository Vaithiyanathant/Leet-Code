class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ze = 0
        on = 0
        cnt = 0
        cnt0 = 0
        for i in range(len(s)):
            if s[i] == "1":
                cnt+=1
                on = max(on,cnt)
                cnt0=0
            else:
                cnt = 0
                cnt0+=1
                ze = max(ze,cnt0)
        return 1 if on > ze else 0
