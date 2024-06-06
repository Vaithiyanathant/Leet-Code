class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        lst = [[0]*len(words) for _ in range(27)]

        s = " ".join(words)
        flag  = 0
        for i in words:
            for j in i:
                lst[ord(j)-97][flag]+=1
            flag+=1
        print(lst)
        ans =  ""
        for k in range(len(lst)):
            if lst[k]!=[0]*len(words):
                l = min(lst[k])
                ans+=(chr(k+97))*l
        print(ans)
        return list(ans)
