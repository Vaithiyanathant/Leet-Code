class Solution:
    def secondHighest(self, s: str) -> int:
        ma = -1
        scma = -1
        for i in range(len(s)):
            if s[i].isdigit():
                a = int(s[i])
                if a > ma:
                    scma = ma
                    ma = a
                elif a > scma and a != ma:
                    scma = a
                    
        return scma

