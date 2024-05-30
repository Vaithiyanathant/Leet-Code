class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        I = 0
        d = len(s)
        res = []
        for i in s:
            if i == 'I':
                res.append(I)
                I+=1
            else:
                res.append(d)
                d-=1
        res.append(I)
        return res