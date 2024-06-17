class Solution:
    def myPow(self, x: float, n: int) -> float:
        def check(n,x,ans):
            if n==0:
                return ans
            if n%2==0:
                return check(n//2,x*x,ans)
            if n%2==1:
                return check(n-1,x,ans*x)
        if n==0:
            return 1
        if n<0:
            x = 1/x
            n = abs(n)
        ans = 1
        return check(n,x,ans)        