class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def check(s,o,c):
            if (o==n and c==n):
                res.append(s)
            #open
            if o<n:
                check(s+"(",o+1,c)
            #close
            if c<o:
                check(s+")",o,c+1)
        res = [ ]
        check("",0,0)
        return res
