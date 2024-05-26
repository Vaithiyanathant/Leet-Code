class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        d=[]
        cnt = 1
        word+="A"
        for i in range(len(word)-1):
            if word[i]!=word[i+1]:
                d.append([word[i],cnt])
                cnt = 1
            if word[i]==word[i+1]:
                cnt+=1
        print(d)
        for i in d:
            if i[1]<=9:
                comp+=str(i[1])+i[0]
            else:
                k = i[1] //9
                r = i[1]-(k*9)
                comp+=k*(str(9)+i[0])
                if r!=0:
                    comp+=str(r)+i[0]
        return comp
                
            
        