class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        se  = set("balloon")
        d = {}
        for i in text:
            if i in se:
                if i not in d:
                    d[i] =1
                else:
                    d[i]+=1
        if "l" in d:
            d["l"]  = d["l"]//2
        if "o" in d:
            d["o"] = d["o"]// 2
        mi = 999999
        for i in "balloon":
            if i not in d :
                return 0
            mi = min(mi, d[i])
        return mi