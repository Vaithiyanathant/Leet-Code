class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        f  = ""
        for i in firstWord:
            f+=str(abs(97-ord(i)))
        s = ""
        for j in secondWord:
            s+=str(abs(97-ord(j)))
        t = ""
        for k in targetWord:
            t+=str(abs(97- ord(k)))
        print(f,s,t)
        return True if int(f)+int(s)==int(t) else False