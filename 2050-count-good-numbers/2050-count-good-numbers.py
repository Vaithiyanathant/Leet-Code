class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10**9)+7
        def power(x,n):
            if n==0:
                return 1 
            ans = power(x,n//2)
            ans = (ans*ans)%mod
            if n%2!=0:
                ans = (ans*x)%mod
            return ans

        odd_index  = n//2
        even_index = (n//2)+(n%2)
        return (power(4,odd_index)*power(5,even_index))%mod