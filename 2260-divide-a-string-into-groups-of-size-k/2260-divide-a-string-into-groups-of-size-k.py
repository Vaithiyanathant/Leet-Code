class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        sub = (len(s)%k)
        if sub==0:
            rem = 0
        else:
            rem = k-sub
        print(rem)
        print(s)
        if rem !=0:
            s+=fill*rem
        print(s)
        pre = 0 
        ans = [ ]
        for i in range(1,len(s)+1):
            if i%k==0:
                ans.append(s[pre:i])
                pre = i 
        return ans

