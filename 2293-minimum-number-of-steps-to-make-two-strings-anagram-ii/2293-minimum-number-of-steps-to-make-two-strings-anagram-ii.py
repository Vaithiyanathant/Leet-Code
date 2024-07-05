class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ct = Counter(t)
        cs = Counter(s)
        cnt = 0
        for i in t:
            if i in cs:
                cs[i]-=1
        for j in s:
            if j in ct:
                ct[j]-=1
        print(ct)
        print(cs)   
        cnt = 0
        for key,l in ct.items():
            if l>0:
                cnt+=l
        for key,p in cs.items():
            if p>0:
                cnt+=p
        return cnt