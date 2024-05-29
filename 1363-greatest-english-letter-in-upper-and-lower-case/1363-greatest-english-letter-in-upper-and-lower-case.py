class Solution:
    def greatestLetter(self, s: str) -> str:
        for i in "abcdefghijklmnopqrstuvwxyz"[::-1]:
            if (i.upper() in s )and (i.lower() in s):
                return i.upper()
        return ""

        