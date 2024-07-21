class Solution:
    def doesAliceWin(self, s: str) -> bool:
        ct=0
        st=('a','e','i','o','u')
        for i in s:
            if i in st:
                return True
        return False