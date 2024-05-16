class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        low = 0
        high = len(s)-1
        ls = list(s)
        while(low<=high):
            if s[low]!=s[high]:
                if s[low]<s[high]:
                    ls[high]=s[low]
                else:
                    ls[low]=s[high]
                low+=1
                high-=1
            else:
                low+=1
                high-=1
        return "".join(ls)