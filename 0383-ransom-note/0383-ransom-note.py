class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lst =[0]*26
        for i in ransomNote:
            lst[ord(i)-97]+=1
        for j in magazine:
            lst[ord(j)-97]-=1
        print(lst)
        for k in lst:
            if k>0:
                return False
        return True