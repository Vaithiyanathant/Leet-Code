class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0: return []
        lst = ["","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        if len(digits)==1: return list(lst[int(digits)-1])
        s = ""
        for i in digits:
            s+=lst[int(i)-1]
            s+=" "
        s =  s.split()
        res = [ ]
        if len(digits)==2:
            for i in s[0]:
                for j in s[1]:
                    res.append(i+j)
        if len(digits)==3:
            for i in s[0]:
                for j in s[1]:
                    for k in s[2]:
                        res.append(i+j+k)
        if len(digits)==4:
            for i in s[0]:
                for j in s[1]:
                    for k in s[2]:
                        for l in s[3]:
                            res.append(i+j+k+l)
        return res

        