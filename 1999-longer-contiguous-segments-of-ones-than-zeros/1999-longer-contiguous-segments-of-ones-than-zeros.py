class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        s+="*"
        print(s)
        lst = []
        k = ""
        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                k+=s[i]
                lst.append(k)
                k=""
            else:
                k+=s[i]
        one = 0
        zero = 0
        print(lst)
        for i in lst:
            if i[0]=="1":
                one = max(one,len(i))
            elif i[0]=="0":
                zero = max(zero,len(i))  
        print(one,zero)
        return True if one>zero else False